import unittest

# Dummy data for testing
VALID_DATA = ["apple", "banana", "cherry"]
INVALID_DATA = ["123", "!@#", "$%^"]
MISSING_DATA = []
BOUNDARY_DATA = ["single_value"]


def enrich_data_lookup(data):
    # Dummy lookup enrichment function
    enriched_data = []
    for item in data:
        if item in ["apple", "banana"]:
            enriched_data.append(item + "_fresh")
        else:
            enriched_data.append(item)
    return enriched_data


def enrich_data_transformation(data):
    # Dummy transformation enrichment function
    return [item.upper() for item in data]


class TestEnrichmentScenarios(unittest.TestCase):

    def test_valid_data_enrichment_lookup(self):
        result = enrich_data_lookup(VALID_DATA)
        self.assertEqual(result, ["apple_fresh", "banana_fresh", "cherry"])

    def test_invalid_data_enrichment_lookup(self):
        result = enrich_data_lookup(INVALID_DATA)
        self.assertEqual(result, ["123", "!@#", "$%^"])

    def test_missing_data_enrichment_lookup(self):
        result = enrich_data_lookup(MISSING_DATA)
        self.assertEqual(result, [])

    def test_boundary_data_enrichment_lookup(self):
        result = enrich_data_lookup(BOUNDARY_DATA)
        self.assertEqual(result, ["single_value"])

    def test_valid_data_enrichment_transformation(self):
        result = enrich_data_transformation(VALID_DATA)
        self.assertEqual(result, ["APPLE", "BANANA", "CHERRY"])

    def test_invalid_data_enrichment_transformation(self):
        result = enrich_data_transformation(INVALID_DATA)
        self.assertEqual(result, ["123", "!@#", "$%^"])

    def test_missing_data_enrichment_transformation(self):
        result = enrich_data_transformation(MISSING_DATA)
        self.assertEqual(result, [])

    def test_boundary_data_enrichment_transformation(self):
        result = enrich_data_transformation(BOUNDARY_DATA)
        self.assertEqual(result, ["SINGLE_VALUE"])


if __name__ == '__main__':
    unittest.main()
