
import pandas as pd
import pytest

from src.customer_churn.clean_data import clean_customer_data


def sample_df():
    return pd.DataFrame({
        "customerID": ["C1", "C2"],
        "tenure": [0, 12],
        "TotalCharges": ["", "120.50"]
    })


def test_blank_total_charges_for_zero_tenure_becomes_zero():
    cleaned = clean_customer_data(sample_df())

    assert cleaned.loc[0, "TotalCharges"] == 0.0
    assert bool(cleaned.loc[0, "TotalCharges_was_blank"]) is True


def test_total_charges_are_numeric_and_not_missing():
    cleaned = clean_customer_data(sample_df())

    assert pd.api.types.is_float_dtype(cleaned["TotalCharges"])
    assert cleaned["TotalCharges"].notna().all()


def test_blank_total_charges_with_nonzero_tenure_raises():
    df = sample_df()
    df.loc[1, "TotalCharges"] = ""

    with pytest.raises(ValueError, match="zero tenure"):
        clean_customer_data(df)


def test_invalid_nonblank_total_charges_raises():
    df = sample_df()
    df.loc[1, "TotalCharges"] = "abc"

    with pytest.raises(ValueError, match="non-numeric"):
        clean_customer_data(df)


def test_duplicate_customer_ids_raise():
    df = sample_df()
    df.loc[1, "customerID"] = "C1"

    with pytest.raises(ValueError, match="Duplicate"):
        clean_customer_data(df)
