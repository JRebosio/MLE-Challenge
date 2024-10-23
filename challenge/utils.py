from datetime import datetime
from typing import Union

import numpy as np
import pandas as pd

from challenge.schemas import FlightTypeOption, OperatorOption

TOP_10_FEATURES = [
    "OPERA_Latin American Wings",
    "MES_7",
    "MES_10",
    "OPERA_Grupo LATAM",
    "MES_12",
    "TIPOVUELO_I",
    "MES_4",
    "MES_11",
    "OPERA_Sky Airline",
    "OPERA_Copa Air",
]


def get_min_diff(data: pd.DataFrame):
    fecha_o = datetime.strptime(data["Fecha-O"], "%Y-%m-%d %H:%M:%S")
    fecha_i = datetime.strptime(data["Fecha-I"], "%Y-%m-%d %H:%M:%S")
    min_diff = ((fecha_o - fecha_i).total_seconds()) / 60
    return min_diff


def get_target(data: pd.DataFrame, target_column: str) -> Union[pd.DataFrame, None]:
    data["min_diff"] = data.apply(get_min_diff, axis=1)
    threshold_in_minutes = 15
    data[target_column] = np.where(data["min_diff"] > threshold_in_minutes, 1, 0)
    target = data[[target_column]]
    return target


def get_features(data: pd.DataFrame) -> pd.DataFrame:
    operator_categories = [operator.value for operator in OperatorOption]
    flight_type_categories = [flight_type.value for flight_type in FlightTypeOption]

    data["OPERA"] = pd.Categorical(data["OPERA"], categories=operator_categories)
    data["TIPOVUELO"] = pd.Categorical(data["TIPOVUELO"], categories=flight_type_categories)
    data["MES"] = pd.Categorical(data["MES"], categories=list(range(1, 13)))

    features = pd.concat(
        [
            pd.get_dummies(data["OPERA"], prefix="OPERA"),
            pd.get_dummies(data["TIPOVUELO"], prefix="TIPOVUELO"),
            pd.get_dummies(data["MES"], prefix="MES"),
        ],
        axis=1,
    )

    features = features[TOP_10_FEATURES]
    return features
