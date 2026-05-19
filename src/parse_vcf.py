import pandas as pd


def parse_vcf(file_path: str) -> pd.DataFrame:
    records = []

    with open(file_path, "r") as file:
        for line in file:
            if line.startswith("##"):
                continue
            if line.startswith("#CHROM"):
                continue

            parts = line.strip().split("\t")

            if len(parts) < 5:
                continue

            records.append({
                "chromosome": parts[0],
                "position": int(parts[1]),
                "variant_id": parts[2],
                "ref": parts[3],
                "alt": parts[4],
            })

    return pd.DataFrame(records)