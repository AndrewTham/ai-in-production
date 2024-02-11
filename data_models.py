from pydantic import BaseModel
from typing import Iterable, List


class Request(BaseModel):
    message: str
    history: List[str]


class Result(BaseModel):
    text_stream: Iterable


class Response(BaseModel):
    result: Result
