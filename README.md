# Data Collection and Pre-processing

This project applies a 12-step data engineering workflow to 500 sales records.
It uses pandas, dictionaries, sets, functions, and a reusable Python class.
The notebook profiles data, cleans whitespace, transforms dates, and creates features.
Required customer, coupon, and city fields are explicitly synthetic.
Country metadata supports a dual-source data dictionary and naming review.
Validated CSV and JSON exports make the prepared data reusable.

## Quick start

Run these commands from the repository root on Windows:

    py -3.12 -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python -m pip install -r requirements.txt
    jupyter notebook

Open `DataCollection_Preprocessing.ipynb`, select the project environment,
and run all cells from top to bottom.

## Project files

- `DataCollection_Preprocessing.ipynb`: documented workflow and results.
- `src/sales_record.py`: reusable sales-record class and constructor function.
- `data/`: original sales data and secondary country reference files.
- `data/processed/`: generated CSV and JSON transaction exports.
- `requirements.txt`: environment dependencies.

## Data sources

- [Excel BI Analytics sales data](https://excelbianalytics.com/downloads-18-sample-csv-files-data-sets-for-testing-sales/)
- [Country Codes reference data](https://github.com/datasets/country-codes)
- [Country Codes field definitions](https://github.com/datasets/country-codes/blob/main/datapackage.yml)

The primary dataset is synthetic. Additional fictional customer IDs,
cities, and coupons use deterministic patterns. Three separate controlled
examples demonstrate whitespace, missing-coupon, and coupon-casing fixes.
Country metadata is used for documentation and name matching; it does not
establish actual shipping destinations.

## Analytical insight

Within the selected 500 records, Papua New Guinea has the highest reported
revenue: 15,629,197.78, approximately 2.20% of the total.
This describes the synthetic sample, not actual market performance.

## Other projects

- [DataEngineeringOne](https://github.com/antoniosg2025-stack/DataEngineeringOne)