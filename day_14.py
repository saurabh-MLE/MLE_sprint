from functools import reduce

cleared_revenues = [18.0, 22.5, 34.5]

accumulate_sum = lambda x,y : x+y
total_pipeline_yield = reduce(accumulate_sum, cleared_revenues)

if __name__ == "__main__":
    print(f"Individual Values: {cleared_revenues} and their Sum: {total_pipeline_yield}")