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
