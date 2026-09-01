model_logs =[{"task" : "image_ocr", "latency" : 250},
             {"task" : "text_generation", "latency" : 1200},
             {"task" : "speech_to_text", "latency" : 480}]

sorted_latency_profile = sorted(model_logs, key = lambda x: x["latency"], reverse = True)

if __name__ == "__main__":
    print(f"UNSORTED LIST: {model_logs}\nSORTED LIST: {sorted_latency_profile}")
    