# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import pandas as pd
import pytest

# IMPORTATION INTERNAL
from gamestonk_terminal.stocks.due_diligence import business_insider_model

@pytest.mark.default_cassette("test_get_price_target_from_analysts_TSLA")
@pytest.mark.vcr
def test_get_price_target_from_analysts(default_csv_path):
    result_df = business_insider_model.get_price_target_from_analysts(ticker="TSLA")
    expected_df = pd.read_csv(default_csv_path, index_col="Date", parse_dates=["Date"])

    pd.testing.assert_frame_equal(result_df, expected_df)


@pytest.mark.default_cassette("test_get_price_target_from_analysts_TSLA")
@pytest.mark.vcr
def test_get_estimates_year_estimates(default_csv_path):
    df_year_estimates, _, _ = business_insider_model.get_estimates(ticker="TSLA")
    expected_df = pd.read_csv(default_csv_path, index_col="YEARLY ESTIMATES")

    pd.testing.assert_frame_equal(df_year_estimates, expected_df)


@pytest.mark.default_cassette("test_get_price_target_from_analysts_TSLA")
@pytest.mark.vcr
def test_get_estimates_quarter_earnings(default_csv_path):
    _, df_quarter_earnings, _ = business_insider_model.get_estimates(ticker="TSLA")
    expected_df = pd.read_csv(default_csv_path, index_col="QUARTER EARNINGS ESTIMATES")

    pd.testing.assert_frame_equal(df_quarter_earnings, expected_df)


@pytest.mark.default_cassette("test_get_price_target_from_analysts_TSLA")
@pytest.mark.vcr
def test_get_estimates_quarter_revenues(default_csv_path):
    _, _, df_quarter_revenues = business_insider_model.get_estimates(ticker="TSLA")
    expected_df = pd.read_csv(default_csv_path, index_col="QUARTER REVENUES ESTIMATES")

    pd.testing.assert_frame_equal(df_quarter_revenues, expected_df)
