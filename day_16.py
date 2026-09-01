api_response_times = [45, 220, 80, 310, 15, 450, 95]

stressed_high_latencies = [n*2 for n in api_response_times if n > 90 ]

if __name__ == "__main__":
    print(f"API response time: {api_response_times}\nResponse time during high stressed latencies: {stressed_high_latencies}")