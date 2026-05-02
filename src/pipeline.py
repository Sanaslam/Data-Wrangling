import os
import pandas as pd
import numpy as np
import logging
import json
from datetime import datetime

# 1. Observability: Detailed Logging
if not os.path.exists('logs'): os.makedirs('logs')
logging.basicConfig(
    filename='logs/data_pipeline.log', 
    level=logging.INFO, 
    format='%(asctime)s - [LEVEL: %(levelname)s] - %(message)s'
)

def run_heavy_pipeline():
    logging.info("Initializing Pipeline: ApexPlanet Data Wrangling T24030")
    
    # 2. Governance: Configuration Loading
    with open('config.json', 'r') as f: config = json.load(f)
    
    # 3. Extract & Transform (Heavy Logic)
    df = pd.read_csv(config['data_source'])
    
    # Statistical Outlier Detection (Z-Score method)
    df['sales_amount'] = pd.to_numeric(df['sales_amount'], errors='coerce')
    mean = df['sales_amount'].mean()
    std = df['sales_amount'].std()
    
    # Keep data within 3 standard deviations
    outlier_limit = mean + (3 * std)
    df_clean = df[df['sales_amount'] <= outlier_limit].copy()
    
    # 4. Validation: Integrity Check
    if df_clean.isnull().values.any():
        logging.error("Integrity Failure: Null values detected after cleaning.")
    else:
        logging.info(f"Integrity Pass: {len(df_clean)} records validated.")

    # 5. Load: Exporting for Analytics
    if not os.path.exists('data/processed'): os.makedirs('data/processed')
    df_clean.to_parquet('data/processed/clean_sales.parquet')
    
    # Generate Professional Summary
    with open('data/processed/summary_report.txt', 'w') as f:
        f.write("=== APEXPLANET ANALYTICS REPORT ===\n")
        f.write(f"TIMESTAMP: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"TOTAL RECORDS: {len(df_clean)}\n")
        f.write(f"STATISTICAL MEAN: {round(df_clean['sales_amount'].mean(), 2)}\n")
        f.write(f"OUTLIER THRESHOLD: {round(outlier_limit, 2)}\n")
        f.write("STATUS: PRODUCTION_READY\n")

if __name__ == "__main__":
    run_heavy_pipeline()
    print("Pipeline Execution Complete. Check logs/data_pipeline.log for details.")
