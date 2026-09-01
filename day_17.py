raw_salaries = {"Sauranh" : 15, "Amit" : 4, "Rahul" : 8, "Vikas" : 18}

filtered_net_payouts = {k:v * 0.90 for k,v in raw_salaries.items() if v > 5}

if __name__ == "__main__":
    print(f"Raw Salaries: {raw_salaries}\nSalaries after net tax deduction: {filtered_net_payouts}")
