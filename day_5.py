def calculate_global_pakage(lpa_amount):
    usd_conversion_rate = 85.50

    inr_total_salary = lpa_amount * 100000
    usd_total_salary = inr_total_salary / usd_conversion_rate
    monthly_inr_takehome = inr_total_salary / 12

    salary_breakdown = {
        "raw_lpa" : lpa_amount,
        "total_inr" : inr_total_salary,
        "total_usd" : round(usd_total_salary, 2),
        "monthly_inr" : round(monthly_inr_takehome, 2)
    }

    return salary_breakdown

if __name__ == "__main__" :
    print("\n" + "="*50)
    print("GLOBAL SALARY CALCULATER MODULE ACTIVE")
    print("="*50)

    target_salary = 15
    my_metrics = calculate_global_pakage(target_salary)

    print(f"Target Threshold : {my_metrics['raw_lpa']} LPA")
    print(f"Total Base Pool : ₹{my_metrics['total_inr']}")
    print(f"Global Value : ${my_metrics['total_usd']} USd")
    print(f"Est. Take-Home : ₹{my_metrics['monthly_inr']} / Month")
    print("="*50 + "\n")
