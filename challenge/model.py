from typing import List, Tuple, Union

import joblib
import pandas as pd

from challenge.utils import get_features, get_target


class DelayModel:

    def __init__(self):
        self._model = joblib.load(
            "xgb_model.joblib"
        )  # Model should be saved in this attribute.

    def preprocess(
        self, data: pd.DataFrame, target_column: str = None
    ) -> Union[Tuple[pd.DataFrame, pd.DataFrame], pd.DataFrame]:
        """
        Prepare raw data for training or predict.

        Args:
            data (pd.DataFrame): raw data.
            target_column (str, optional): if set, the target is returned.

        Returns:
            Tuple[pd.DataFrame, pd.DataFrame]: features and target.
            or
            pd.DataFrame: features.
        """
        features = get_features(data)

        if target_column is None:
            return features

        target = get_target(data, target_column)

        return features, target

    def fit(self, features: pd.DataFrame, target: pd.DataFrame) -> None:
        """
        Fit model with preprocessed data.

        Args:
            features (pd.DataFrame): preprocessed data.
            target (pd.DataFrame): target.
        """
        self._model.fit(features, target)
        return

    def predict(self, features: pd.DataFrame) -> List[int]:
        """
        Predict delays for new flights.

        Args:
            features (pd.DataFrame): preprocessed data.

        Returns:
            (List[int]): predicted targets.
        """
        return self._model.predict(features).tolist()
