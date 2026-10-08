from pydantic import BaseModel


class Transaction(BaseModel):
    amt: float
    lat: float
    long: float
    city_pop: int
    merch_lat: float
    merch_long: float

    merchant: str
    category: str
    gender: str
    state: str
    job: str


class CardFeatures(BaseModel):
    distance_km: float
    card_transaction_count: int
    card_fraud_count: int
    card_fraud_rate: float
    card_avg_amount: float | None = None


class FraudDetectionInferenceInput(BaseModel):
    transaction: Transaction
    card_features: CardFeatures


class FraudDetectionInferenceOutput(BaseModel):
    fraud_probability: float
    fraud_prediction: bool