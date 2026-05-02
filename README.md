ApexPlanet Data Wrangling | Sales Processing System

Developed by: Sana Khan (Intern, Data Analytics)

1. Project Overview

This repository contains a production-ready, automated ETL (Extract, Transform, Load) pipeline designed to streamline raw sales data. The system automatically ingests, validates, cleans, and visualises transaction data, ensuring data integrity for downstream analytics.

Key Technical Pillars:

// Statistical Anomaly Detection: Utilises a 3-sigma (Z-Score) thresholding logic to automatically filter out sales outliers.

// Production-Grade Logging: Maintains a full audit trail of every pipeline run to ensure transparency and debugging efficiency.

// Optimised Storage: Transforms raw CSV data into Parquet format for high-performance query execution and reduced storage footprint.

// Interactive Visualisation: Integrated Streamlit dashboard for real-time business intelligence and trend analysis.





2. Directory Structure 

DataWrangling/
├── data/
│   ├── raw/                # Source sales_transactions.csv
│   └── processed/          # Cleaned .parquet and summary reports
├── logs/                   # System audit trails and error logs
├── src/
│   ├── pipeline.py         # Core ETL logic
│   └── dashboard.py        # Streamlit visualization interface
├── config.json             # System configuration and thresholds
└── README.md





3. Getting Started

Prerequisites
Ensure you have Python 3.13+ installed. Install the required dependencies:
// COMMAND.
pip install pandas streamlit

Execution Guide-

The "Engine" (The Pipeline)

1.cd Desktop/DataWrangling
2.cat src/pipeline.py 
3.python3 src/pipeline.py


The "Audit" (Logging & Results)

4. ls data/processed
5. cat data/processed/summary_report.txt
6. cat logs/data_pipeline.log


The "Wow" Factor (The Dashboard)
7. python3 -m streamlit run src/dashboard.py





4. Business Impact

This pipeline eliminates manual data cleaning workflows, reducing processing time by [X]% and ensuring that the analytics team always works with validated, production-ready datasets.
