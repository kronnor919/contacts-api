from dataclasses import dataclass
from http import HTTPStatus

SQLITE_DB_URI = "sqlite:///sqlite3_testdb.db"

# Agregar soporte para codificacion universal utf-8. No se pueden devolver tildes
INTERNAL_SERVER_ERROR_MESSAGE = "A ocurrido un error interno en el servidor, esto puede ser debido a que se encuentre en mantenimiento o alguna otra causa. Informacion del error: %s"

def generate_server_error(error: str) -> str:
    return INTERNAL_SERVER_ERROR_MESSAGE % error + "." if not error.endswith(".") else ""

@dataclass
class Result[T]:
    payload: T | None
    error: str | None
    is_success: bool
    
    @staticmethod
    def success(payload: T) -> "Result[T]":
        return Result[T](payload, None, True)

    @staticmethod
    def failure(error: str) -> "Result[T]":
        return Result[T](None, error, False)

@dataclass
class HTTPResult[T]:
    payload: T | None
    error: str | None
    is_success: bool
    status_code: int
    
    @staticmethod
    def success(payload: T, status_code: int) -> "HTTPResult[T]":
        return HTTPResult[T](payload, None, True, status_code)
    
    @staticmethod
    def failure(error: str, status_code: int) -> "HTTPResult[T]":
        return HTTPResult[T](None, error, False, status_code)
