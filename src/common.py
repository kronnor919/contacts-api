from dataclasses import dataclass


SQLITE_DB_URI = "sqlite:///sqlite3_testdb.db"

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
class HttpResult[T]:
    payload: T | None
    error: str | None
    is_success: bool
    status_code: int
    
    @staticmethod
    def success(payload: T, status_code: int) -> "HttpResult[T]":
        return HttpResult[T](payload, None, True, status_code)
    
    @staticmethod
    def failure(error: str, status_code: int) -> "HttpResult[T]":
        return HttpResult[T](None, error, False, status_code)
