import joblib
import pandas as pd


def test_model_prediction():
    model = joblib.load("models/model.pkl")
    columns = joblib.load("models/columns.pkl")

    # Create a DataFrame instead of np.array to match training structure
    test_input = pd.DataFrame([[5, 85, 1]], columns=columns)

    prediction = model.predict(test_input)

    assert prediction.shape == (1,)
    assert prediction[0] > 0  # Should be a valid score