import pandas as pd
from src.ensembl_client import get_variant_overlap


def annotate_variants(variants: pd.DataFrame) -> pd.DataFrame:
    annotated_records = []

    for _, row in variants.iterrows():
        annotation = get_variant_overlap(
            chromosome=str(row["chromosome"]),
            position=int(row["position"])
        )

        record = row.to_dict()
        record.update(annotation)

        annotated_records.append(record)

    return pd.DataFrame(annotated_records)