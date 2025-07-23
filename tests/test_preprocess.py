from src import preprocess


def test_clean_data_columns():
    df = preprocess.clean_data()
    assert "study_time" in df.columns
    assert "attendance" in df.columns
    assert "gender" in df.columns
    assert "score" in df.columns
    assert df.isnull().sum().sum() == 0