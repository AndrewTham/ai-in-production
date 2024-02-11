from fastapi import FastAPI

from data_models import Response, Request, Result
from predict import predict

fastapi_app = FastAPI()


@fastapi_app.post("/predict", response_model=Response)
async def predict_api(request: Request):
    result = predict(request.question)
    return Response(result=Result(text=result))
