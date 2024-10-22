from enum import Enum

from pydantic import BaseModel, Field


class OperatorOption(str, Enum):
    GRUPO_LATAM = "Grupo LATAM"
    SKY_AIRLINE = "Sky Airline"
    AEROLINEAS_ARGENTINAS = "Aerolineas Argentinas"
    COPA_AIR = "Copa Air"
    LATIN_AMERICAN_WINGS = "Latin American Wings"
    AVIANCA = "Avianca"
    JETSMART_SPA = "JetSmart SPA"
    GOL_TRANS = "Gol Trans"
    AMERICAN_AIRLINES = "American Airlines"
    AIR_CANADA = "Air Canada"
    IBERIA = "Iberia"
    DELTA_AIR = "Delta Air"
    AIR_FRANCE = "Air France"
    AEROMEXICO = "Aeromexico"
    UNITED_AIRLINES = "United Airlines"
    OCEANAIR_LINHAS_AEREAS = "Oceanair Linhas Aereas"
    ALITALIA = "Alitalia"
    KLM = "K.L.M."
    BRITISH_AIRWAYS = "British Airways"
    QANTAS_AIRWAYS = "Qantas Airways"
    LACSA = "Lacsa"
    AUSTRAL = "Austral"
    PLUS_ULTRA_LINEAS_AEREAS = "Plus Ultra Lineas Aereas"


class FlightTypeOption(str, Enum):
    International = "I"
    National = "N"


class Flight(BaseModel):
    OPERA: OperatorOption
    TIPOVUELO: FlightTypeOption
    MES: int = Field(description="Number of month", ge=1, le=12)


class Data(BaseModel):
    flights: list[Flight]


class FlightsPrediction(BaseModel):
    predict: list[int]
