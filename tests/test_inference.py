from fraud_detection_contracts import (
    CardFeatures,
    FraudDetectionInferenceInput,
    Transaction,
)


def test_inference_input() -> None:
    input_data = FraudDetectionInferenceInput(
        transaction=Transaction(
            amt=123.45,
            lat=40.1,
            long=-73.2,
            city_pop=12345,
            merch_lat=40.2,
            merch_long=-73.1,
            merchant="merchant_x",
            category="shopping_net",
            gender="M",
            state="NY",
            job="Engineer",
        ),
        card_features=CardFeatures(
            distance_km=12.4,
            card_transaction_count=17,
            card_fraud_count=2,
            card_fraud_rate=0.1176,
            card_avg_amount=84.31,
        ),
    )

    assert input_data.transaction.amt == 123.45
    assert input_data.card_features.card_transaction_count == 17