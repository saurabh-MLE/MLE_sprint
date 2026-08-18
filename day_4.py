project_files = ["dataset_v1.csv","uncleanwd_logs.txt","model_weights.bin","config.json"]

print("\n" + "="*50)
print("AUTOMATED BATCH INGESTION PIPELINE ACTIVE")
print("="*50)

file_count = 0

for file in project_files:
    file_count += 1

    if file.endswith(".csv"):
        status = "CRITICAL DATA : SENT TO CLEANING PIPELINE"
    elif file.endswith(".bin"):
        status = "AI MODEL WEIGHTS : SENT TO DEPLOYMENT ENGINE"
    else:
        status = "STANDARD FILE : ARCHIVED"

    print(f"File # {file_count} : {file} -> Status : {status}")

print("="*50)
print(f"SUCCESS : ALL {file_count} FILES PROCESSED SUCCESSFULLY.")
print("="*50 + "\n")

