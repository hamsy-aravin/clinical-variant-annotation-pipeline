# Clinical Variant Annotation Pipeline

![Python Tests](https://github.com/hamsy-aravin/clinical-variant-annotation-pipeline/actions/workflows/python-tests.yml/badge.svg)

## Overview

This project is a Python-based clinical genomics pipeline designed to parse Variant Call Format (VCF) files, annotate genomic variants using the Ensembl REST API, and prioritise clinically relevant variants through automated workflows.

The pipeline demonstrates key bioinformatics engineering concepts including:

- genomic data parsing
- variant annotation
- biological data integration
- reproducible workflows
- automated testing
- CI/CD with GitHub Actions

This project was developed as a portfolio project to strengthen practical experience in computational genomics, clinical bioinformatics, and bioinformatics engineering.

---

## Features

- Parse VCF files containing genomic variants
- Query the Ensembl REST API for gene annotation
- Annotate variants with gene-level information
- Prioritise variants using biologically relevant rules
- Generate structured CSV and JSON reports
- Automated testing using `pytest`
- CI/CD pipeline using GitHub Actions

---

## Tech Stack

| Area | Tools |
|---|---|
| Programming | Python |
| Genomics | VCF, Ensembl REST API |
| Data Handling | pandas |
| Testing | pytest |
| CI/CD | GitHub Actions |
| Version Control | Git & GitHub |

---

## Repository Structure

```text
clinical-variant-annotation-pipeline/
├── src/
├── tests/
├── data/
├── outputs/
├── .github/workflows/
├── main.py
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## Example Workflow

### Input

The pipeline accepts genomic variants stored in a VCF file:

```vcf
#CHROM  POS         REF ALT
7        140453136  A   T
17       43071077   G   A
```

### Processing

The pipeline:

1. Parses the VCF file
2. Extracts variant coordinates
3. Queries the Ensembl REST API
4. Annotates variants with gene information
5. Prioritises clinically relevant variants
6. Generates structured output reports

---

## Example Output

### Annotated Variants

| chromosome | position | gene_symbol | priority |
|---|---|---|---|
| 17 | 43071077 | BRCA1 | High |
| 7 | 140453136 | EGFR | High |

### Summary JSON

```json
{
    "total_variants": 3,
    "annotated_variants": 2,
    "high_priority_variants": 2
}
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/hamsy-aravin/clinical-variant-annotation-pipeline.git
cd clinical-variant-annotation-pipeline
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Pipeline

Run the main workflow:

```bash
python3 main.py
```

Generated outputs will appear in:

```text
outputs/
```

---

## Running Tests

Run automated tests using:

```bash
python3 -m pytest
```

---

## CI/CD

GitHub Actions is used to automatically:

- install dependencies
- run tests
- validate workflow reproducibility

The pipeline is automatically tested on every push to the repository.

---

## Future Improvements

Potential future developments include:

- ClinVar integration
- gnomAD allele frequency annotation
- Variant Effect Predictor (VEP) integration
- Docker containerisation
- FastAPI deployment
- Nextflow workflow integration
- Clinical pathogenicity scoring
- Interactive dashboard visualisation

---

## Author

Hamsathvani Aravinthan

MSc Bioinformatics — Queen Mary University of London

Interests:
- Clinical Bioinformatics
- Computational Genomics
- Cancer Bioinformatics
- Knowledge Graphs
- Translational Genomics
