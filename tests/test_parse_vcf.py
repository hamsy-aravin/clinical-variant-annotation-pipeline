from src.parse_vcf import parse_vcf


def test_parse_vcf():
    df = parse_vcf("data/example_variants.vcf")

    assert len(df) == 3
    assert "chromosome" in df.columns
    assert "position" in df.columns
    assert "ref" in df.columns
    assert "alt" in df.columns