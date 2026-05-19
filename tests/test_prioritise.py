import pandas as pd
from src.prioritise_variants import prioritise_variants


def test_prioritise_variants():
    df = pd.DataFrame([
        {"gene_symbol": "TP53"},
        {"gene_symbol": "UNKNOWN"},
        {"gene_symbol": None}
    ])

    result = prioritise_variants(df)

    assert result.loc[0, "priority"] == "High"
    assert result.loc[1, "priority"] == "Medium"
    assert result.loc[2, "priority"] == "Low"