from pydantic import BaseModel
from typing import List


class Request(BaseModel):
    question: str


class Result(BaseModel):
    text: str


class Response(BaseModel):
    result: Result
