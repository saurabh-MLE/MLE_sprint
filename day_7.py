alert = "ALERT : Core AI Model Inference Endpoint running at 94% Capacity."

with open("server_logs.txt", "w") as f:
    f.write(alert)

print("\n" + "="*50)
print("[SYSTEM] Server log file written successfully.\n")

with open("server_logs.txt") as f:
    log_content = f.read()

print(f"EXTRACTED DATA {log_content}")
print("="*50 + "\n")