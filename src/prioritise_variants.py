import pandas as pd


CANCER_GENES = {
    "TP53",
    "BRCA1",
    "BRCA2",
    "EGFR",
    "KRAS",
    "PIK3CA"
}


def prioritise_variants(annotated_df: pd.DataFrame) -> pd.DataFrame:
    df = annotated_df.copy()

    def assign_priority(row):
        gene = row.get("gene_symbol")

        if gene in CANCER_GENES:
            return "High"

        if pd.notna(gene):
            return "Medium"

        return "Low"

    df["priority"] = df.apply(assign_priority, axis=1)

    return df