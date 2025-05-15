
# FIELD_DICTIONARY_DESIGN.md

## Purpose

This document defines the **design, requirements, and conceptual validation** of the **Field Dictionary** prototype for statistical property collection, as part of the work on the **federated dataset comparison engine**.  
The dictionary is designed to store key statistical metadata for each data field from datasets such as MIMIC-III, supporting similarity assessments (e.g., using Wasserstein distance) in the federated learning context.

## Requirements

- **Objective:** Define a **standardized and extensible format** to represent statistical summaries for different data types:
  - Numerical continuous (e.g., lab values, measurements)
  - Categorical nominal (e.g., medication names, activity levels)

- **Statistical properties to be stored:**
  - For **numerical continuous fields:**
    - `mean`, `median`, `std_dev`, `variance`
    - `quartile_1`, `quartile_3`, `percentile_5`, `percentile_95`
    - `skewness`, `kurtosis`
    - `histogram` (`bins`, `counts`)
    - `distribution_fit`
  - For **categorical fields:**
    - `mode`, `mode_frequency`
    - `category_frequencies`
    - `entropy`

- **Input:** Sample values extracted from a dataset field.

- **Output format:** JSON structure per field, using snake_case naming convention.

## JSON Schema Example

```json
{
  "field_name": "example_field",
  "data_type": "numerical_continuous",
  "source_dataset_id": "dataset_name",
  "sample_values_preview": [ ... ],
  "count": ...,
  "unique_count": ...,
  "missing_count": ...,
  "mean": ...,
  "median": ...,
  "std_dev": ...,
  "variance": ...,
  "quartile_1": ...,
  "quartile_3": ...,
  "percentile_5": ...,
  "percentile_95": ...,
  "skewness": ...,
  "kurtosis": ...,
  "histogram": {
    "bins": [ ... ],
    "counts": [ ... ]
  },
  "distribution_fit": {
    "type": "...",
    "parameters": { ... },
    "fit_score": null
  }
}
```

## Conceptual Test with MIMIC-III Fields

### Example 1 — Numerical continuous field: `age`

```json
{
  "field_name": "age",
  "data_type": "numerical_continuous",
  "source_dataset_id": "mimiciv_3_1_derived_export_age_data.csv",
  "sample_values_preview": [76, 18, 33, 68, 80, 52, 89, 74, 86, 79],
  "count": 10,
  "unique_count": 10,
  "missing_count": 0,
  "mean": 65.5,
  "median": 75.0,
  "std_dev": 23.47,
  "variance": 551.03,
  "quartile_1": 52.0,
  "quartile_3": 86.0,
  "percentile_5": 18.45,
  "percentile_95": 88.55,
  "skewness": -1.1861,
  "kurtosis": -0.6561,
  "histogram": {
    "bins": [18.0, 26.2, 34.4, 42.6, 50.8, 59.0, 67.2, 75.4, 83.6, 91.8, 100.0],
    "counts": [1, 1, 0, 0, 1, 1, 2, 2, 2, 0]
  },
  "distribution_fit": {
    "type": "normal",
    "parameters": {
      "mean": 65.5,
      "std_dev": 23.47
    },
    "fit_score": null
  }
}
```

### Example 2 — Categorical field: `acei`

```json
{
  "field_name": "acei",
  "data_type": "categorical",
  "source_dataset_id": "mimiciv_3_1_derived_export_acei_data.csv",
  "sample_values_preview": [
    "Captopril",
    "Lisinopril",
    "Captopril",
    "Benazepril",
    "Lisinopril",
    "Benazepril",
    "Captopril",
    "Lisinopril",
    "Captopril",
    "Lisinopril"
  ],
  "count": 10,
  "unique_count": 3,
  "missing_count": 0,
  "mode": "Captopril",
  "mode_frequency": 4,
  "category_frequencies": {
    "Captopril": 4,
    "Lisinopril": 4,
    "Benazepril": 2
  },
  "entropy": 1.571
}
```

## Notes

- The dictionary has been tested conceptually with real MIMIC-III data samples.
- The chosen JSON structure is flexible and supports both numerical and categorical fields.
- This format will serve as the foundation for later automation and integration into the federated matching engine.


## Rationale & Considerations

### Rationale for Statistical Properties Selection

| Metric             | Rationale                                                                                         |
|--------------------|---------------------------------------------------------------------------------------------------|
| `mean`, `median`   | Central tendency indicators, important to assess typical values and detect asymmetries.          |
| `std_dev`, `variance` | Dispersion indicators, fundamental to compare variability between datasets.                   |
| `quartile_1`, `quartile_3`, `percentile_5`, `percentile_95` | Describe spread and tails, help identify potential outliers and asymmetries. |
| `skewness`         | Third moment; measures asymmetry, essential for detecting skewed distributions.                   |
| `kurtosis`         | Fourth moment; captures tail heaviness or peakedness, complements skewness.                       |
| `histogram`        | Captures the shape of the empirical distribution, enabling visual or statistical comparisons.      |
| `distribution_fit` | Provides a compact parametric approximation (e.g., Normal), useful in scenarios where modeling is needed. |
| `mode`, `mode_frequency` | Key descriptors for categorical fields, providing insight into dominant classes.         |
| `category_frequencies` | Full distribution for categorical fields, enables precise comparison between datasets.     |
| `entropy`          | Information-theoretic measure of dispersion for categorical data; captures concentration vs. spread. |

### Considerations and Limitations (Conceptual Phase)

- The current dictionary and JSON are **conceptual and designed for validation purposes only.**
- The **samples are intentionally small (n=10)**, following the conceptual nature of this task.
- **No automated fit score (e.g., KS test) has been computed**, `fit_score` remains a placeholder.
- **Entropy and higher moments are sensitive to sample size**; their current values are indicative and not statistically robust on such small samples.
- Ordinal fields are **not yet included in this conceptual test**, but the structure is designed to support them in the next phase.


