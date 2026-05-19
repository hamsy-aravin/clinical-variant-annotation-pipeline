from src.parse_vcf import parse_vcf
from src.annotate_variants import annotate_variants
from src.prioritise_variants import prioritise_variants
from src.report import save_outputs


def run_pipeline():
    input_vcf = "data/example_variants.vcf"
    output_csv = "outputs/annotated_variants.csv"
    output_json = "outputs/summary.json"

    variants = parse_vcf(input_vcf)
    annotated = annotate_variants(variants)
    prioritised = prioritise_variants(annotated)

    save_outputs(prioritised, output_csv, output_json)

    print("Pipeline completed successfully.")
    print(prioritised)


if __name__ == "__main__":
    run_pipeline()