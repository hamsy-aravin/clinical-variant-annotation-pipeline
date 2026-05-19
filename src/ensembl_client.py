import requests


ENSEMBL_BASE_URL = "https://rest.ensembl.org"


def get_variant_overlap(chromosome: str, position: int) -> dict:
    region = f"{chromosome}:{position}-{position}"
    url = f"{ENSEMBL_BASE_URL}/overlap/region/human/{region}"

    headers = {
        "Content-Type": "application/json"
    }

    params = {
        "feature": "gene"
    }

    response = requests.get(url, headers=headers, params=params, timeout=20)

    if response.status_code != 200:
        return {
            "gene_symbol": None,
            "gene_id": None,
            "source": "Ensembl REST API",
            "status": "failed"
        }

    data = response.json()

    if not data:
        return {
            "gene_symbol": None,
            "gene_id": None,
            "source": "Ensembl REST API",
            "status": "no_gene_found"
        }

    gene = data[0]

    return {
        "gene_symbol": gene.get("external_name"),
        "gene_id": gene.get("id"),
        "source": "Ensembl REST API",
        "status": "annotated"
    }