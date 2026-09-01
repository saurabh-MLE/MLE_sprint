from functools import reduce

raw_latencies = [40, 120, 80, 200, 50]

filtered_logs = list(filter(lambda n: (n >= 80), raw_latencies))
weighted_logs = list(map(lambda n: round(n*1.5), filtered_logs))
total_severity_score = reduce(lambda x,y: x+y, weighted_logs)

if __name__ == '__main__':
    print(f"Raw Latencies: {raw_latencies}\nFiltered Logs: {filtered_logs}\nWeighted Logs: {weighted_logs}\nTotal Serverity Score: {total_severity_score}")