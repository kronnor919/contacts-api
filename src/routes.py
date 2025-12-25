from typing import Any
from flask import Blueprint, Flask, jsonify, request, url_for
from services import use_contact_service


bp = Blueprint("api", __name__, url_prefix="/api")

@bp.route("/contacts", methods=["GET"])
def all_contacts():
    service = use_contact_service()
    res = service.all()
    
    if not res.is_success:
        return jsonify({
            "success": False,
            "error": res.error,
            "contacts": []
        }), 500
    return jsonify({
        "success": True,
        "error": None,
        "contacts": [
            {
                "id": c.id,
                "tag": c.tag,
                "phone": c.phone,
                "created_at": c.created_at
            }
        for c in res.payload]
    }), 200

@bp.route("/contacts/<int:id>", methods=["GET"])
def get_contact(id: int):
    service = use_contact_service()
    res = service.get(id)
    
    if not res.is_success:
        return jsonify({
            "success": False,
            "error": res.error,
            "contact": None
        }), 500
    
    if not res.payload:
        return jsonify({
            "success": False,
            "error": f"Contact with id {id} do not exists.",
            "contact": None
        }), 404
    
    c = res.payload
    return jsonify({
        "success": True,
        "error": None,
        "contact": {
            "id": c.id,
            "tag": c.tag,
            "phone": c.phone,
            "created_at": c.created_at
        }
    }), 200

@bp.route("/contacts", methods=["POST"])
def post_contact():
    json: dict[str, Any] = request.get_json()
    
    tag: str | None = json.get("tag")
    phone: str | None = json.get("phone")
    
    if tag is None or phone is None:
        return jsonify({
            "success": False,
            "error": "The request is missing parameters ('tag' or 'phone').",
            "contact": None
        }), 400
    
    service = use_contact_service()
    res = service.add(tag, phone)
    
    if not res.is_success:
        return jsonify({
            "success": False,
            "error": res.error,
            "contact": None
        }), 500
    
    c = res.payload
    response = jsonify({
        "success": True,
        "error": None,
        "contact": {
            "id": c.id,
            "tag": c.tag,
            "phone": c.phone,
            "created_at": c.created_at
        }
    })
    response.headers["Location"] = url_for("api.get_contact", id=c.id, _external=True)
    
    return response, 201

@bp.route("/contacts/<int:id>", methods=["DELETE"])
def delete_contact(id: int):
    service = use_contact_service()
    res = service.delete(id)
    
    if not res.is_success:
        return jsonify({
            "success": False,
            "error": res.error,
            "contact": None
        }), 500
    
    
    c = res.payload
    return jsonify({
        "success": True,
        "error": None,
        "contact": {
            "id": c.id,
            "tag": c.tag,
            "phone": c.phone,
            "created_at": c.created_at
        }
    }), 200

def register_routes(app: Flask) -> None:
    app.register_blueprint(bp)