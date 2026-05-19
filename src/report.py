import json
import pandas as pd


def save_outputs(df: pd.DataFrame, output_csv: str, output_json: str) -> None:
    df.to_csv(output_csv, index=False)

    summary = {
        "total_variants": int(len(df)),
        "annotated_variants": int(df["gene_symbol"].notna().sum()),
        "high_priority_variants": int((df["priority"] == "High").sum()),
        "genes_identified": sorted(df["gene_symbol"].dropna().unique().tolist())
    }

    with open(output_json, "w") as file:
        json.dump(summary, file, indent=4)