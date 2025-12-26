# Contacts API

Una API que guarda información básica de contactos, permite agregar, obtener y eliminar (modificar no es soportado por ahora).

## Estructura de un contacto

```json
{
    "id": 10,
    "tag": "Leo",
    "phone": "+53 98989898",
    "created_at": "Wed, 24 Dec 2025 20:06:42 GMT"
}
```

## Estructura básica de las responses

***IMPORTANTE:*** Para los ejemplos usamos la key "contact", pero dependiendo del endpoint puede variar a "contacts", esto se especifica para cada endpoint en la sección [Endpoints](#endpoints).

### Éxito (200, 201)

```json
{
    "success": true,
    "error": null,
    "contact": ... // objeto o array dependiendo del endpoint
}
```

### Error/Rechazo (500, 404, 415, 400)

```json
{
    "success": false,
    "error": "Descripción textual del error.",
    "contact": null // o array vacío dependiendo del endpoint
}
```

## Endpoints

### `GET /api/contacts`

Lista de todos los contactos registrados.

### Response exitosa - 200

```json
{
    "success": true,
    "error": null,
    "contacts": [
        ... 
    ] // array vacío o con representaciones de contactos
}
```

### Error interno - 500

```json
{
    "success": false,
    "error": "Descripción textual del error.",
    "contacts": []
}
```

---

### `GET /api/contacts/<id>`

Obtiene información de un contacto con un id específico.

### Response exitosa - 200

```json
{
    "success": true,
    "error": null,
    "contact": {...}
}
```

### ID inexistente - 404

```json
{
    "success": false,
    "error": "Contact with id <id> do not exists.",
    "contact": null
}
```

### Error interno - 500

```json
{
    "success": false,
    "error": "Descripción textual del error.",
    "contact": null
}
```

---

### `POST /api/contacts`

Registra un nuevo contacto.

### Estructura de request esperada

```json
{
    "tag": "Etiqueta del contacto",
    "phone": "Número telefónico"
}
```

### Response exitosa - 201

```json
{
    "success": true,
    "error": null,
    "contact": {...}
}
```

### Headers

`Location: <domain>/api/contacts/<id>`

### Párametros faltantes - 400

```json
{
    "success": false,
    "error": "The request is missing parameters ('tag' or 'phone').",
    "contact": null
}
```

### Error interno - 500

```json
{
    "success": false,
    "error": "Descripción textual del error.",
    "contact": null
}
```

---

### `DELETE /api/contacts/<id>`

Elimina un contacto registrado. No deja ningún rastro accesible de su información.

### Response exitosa - 200

```json
{
    "success": true,
    "error": null,
    "contact": {...}
}
```

### ID Inexistente - 404

```json
{
    "success": false,
    "error": "Contact with id <id> do not exists.",
    "contact": null
}
```

### Error interno - 500

```json
{
    "success": false,
    "error": "Descripción textual del error.",
    "contact": null
}
```

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
