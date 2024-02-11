from fastapi import FastAPI

from data_models import Response, Request, Result
from chatbot import predict

fastapi_app = FastAPI()


@fastapi_app.post("/predict", response_model=Response)
async def predict_api(request: Request):
    result_stream = predict(request.message, request.history)
    return Response(result=Result(text_stream=result_stream))
