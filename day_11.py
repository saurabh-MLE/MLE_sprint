raw_matrics = ["cpu_utilization:88", "memory_usage:42", "disk_io:12", "network_latency:95"]

cleaned_metris = [n.strip() for n in raw_matrics]

extract_value = lambda n : int(n.split(":")[1])

if __name__ == "__main__":

    for metric in cleaned_metris:
        numerical_value = extract_value(metric)
        output_line = f"Telementry Metric: {metric} --> Extracted Value: {numerical_value}"

        if numerical_value > 85:
            output_line += " [CRITICAL WARNING: THRESHOLD EXCEEDED]"

        print(output_line)

