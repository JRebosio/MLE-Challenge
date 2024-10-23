import fastapi
import pandas as pd
from fastapi import Body, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from challenge.model import DelayModel
from challenge.schemas import Data, FlightsPrediction

app = fastapi.FastAPI()
delay_model = DelayModel()


@app.get("/health", status_code=200)
async def get_health() -> dict:
    return {"status": "OK"}


@app.post("/predict", status_code=200)
async def post_predict(data: Data = Body(..., description="Data to predict")):
    flight_dicts = [flight.dict() for flight in data.flights]
    flights = pd.DataFrame(flight_dicts)

    features = delay_model.preprocess(data=flights)

    predictions = delay_model.predict(features)
    return FlightsPrediction(predict=predictions)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={"detail": exc.errors()},
    )
