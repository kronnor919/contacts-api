from typing import Any, cast
from flask import Blueprint, Flask, jsonify, request, url_for
from entities import Contact
from services import use_contact_service
from common import HTTPStatus, generate_server_error


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
        }), HTTPStatus.INTERNAL_SERVER_ERROR
    
    contacts = cast(list[Contact], res.payload)
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
        for c in contacts]
    }), HTTPStatus.OK

@bp.route("/contacts/<int:id>", methods=["GET"])
def get_contact(id: int):
    service = use_contact_service()
    res = service.get(id)
    
    if not res.is_success:
        return jsonify({
            "success": False,
            "error": res.error,
            "contact": None
        }), HTTPStatus.INTERNAL_SERVER_ERROR
    
    if not res.payload:
        return jsonify({
            "success": False,
            "error": f"Contact with id {id} do not exists.",
            "contact": None
        }), HTTPStatus.NOT_FOUND
    
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
    }), HTTPStatus.OK

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
        }), HTTPStatus.BAD_REQUEST
    
    service = use_contact_service()
    res = service.add(tag, phone)
    
    if not res.is_success:
        return jsonify({
            "success": False,
            "error": res.error,
            "contact": None
        }), HTTPStatus.INTERNAL_SERVER_ERROR
    
    c = cast(Contact, res.payload)
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
    response.status_code = HTTPStatus.CREATED

    return response

@bp.route("/contacts/<int:id>", methods=["DELETE"])
def delete_contact(id: int):
    service = use_contact_service()
    res = service.delete(id)
    
    if not res.is_success:
        if res.status_code == HTTPStatus.NOT_FOUND:
            return jsonify({
                "success": False,
                "error": res.error,
                "contact": None
            }), HTTPStatus.NOT_FOUND
        
        return jsonify({
            "success": False,
            "error": generate_server_error(cast(str, res.error)),
            "contact": None
        }), HTTPStatus.INTERNAL_SERVER_ERROR
    
    
    c = cast(Contact, res.payload)
    return jsonify({
        "success": True,
        "error": None,
        "contact": {
            "id": c.id,
            "tag": c.tag,
            "phone": c.phone,
            "created_at": c.created_at
        }
    }), HTTPStatus.OK

def register_routes(app: Flask) -> None:
    app.register_blueprint(bp)
