from dataclasses import dataclass
from enum import Enum
from http import HTTPStatus

SQLITE_DB_URI = "sqlite:///sqlite3_testdb.db"

# Agregar soporte para codificacion universal utf-8. No se pueden devolver tildes
INTERNAL_SERVER_ERROR_MESSAGE = "A ocurrido un error interno en el servidor, esto puede ser debido a que se encuentre en mantenimiento o alguna otra causa. Informacion del error: %s"

def generate_server_error(error: str) -> str:
    return INTERNAL_SERVER_ERROR_MESSAGE % error + "." if not error.endswith(".") else ""

class CustomStatus(Enum):
    # Success 200 - 299
    OK = 200
    CREATED = 201
    DELETED = 202
    
    # Errors 400 - 499
    VALIDATION_ERR = 400
    DB_NOT_EXISTS = 401
    UNEXPECTED_ERROR = 402

@dataclass
class Result[T]:
    value: T | None
    error: str | None
    is_success: bool
    status: CustomStatus
    
    @staticmethod
    def success(value: T, status: CustomStatus) -> "Result[T]":
        return Result[T](value, None, True, status)
    
    @staticmethod
    def failure(error: str, status: CustomStatus) -> "Result[T]":
        return Result[T](None, error, False, status)
