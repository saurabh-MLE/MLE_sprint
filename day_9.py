import json

portfolio_data = {"username": "saurabh-MLE", "hours": 1020, "projects": 5, "status": "TIER 1"}

with open("pipeline_status.json", "w") as jf:
    json.dump(portfolio_data, jf, indent=4)

print("[INFRA] DAtA pipeline state successfully migrated to JSON storage room")

