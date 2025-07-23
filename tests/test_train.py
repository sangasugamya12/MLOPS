from src import train


def test_train_model_runs():
    try:
        train.train_model()
        assert True
    except Exception as e:
        assert False, f"Training failed: {e}"