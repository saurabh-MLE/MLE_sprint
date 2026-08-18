# --- STEP 1 : MESSY INPUT DATA FROM A USER ---
raw_username = " mEram_Sharma "
raw_target_lpa = "15"
raw_daily_hours = "8.5"
is_committed_input = "True"  # This is a string, not a boolean yet!

# --- STEP 2 : DATA CLEANING AND TYPE CONVERTION ---
# 1. Clean the text string (Remove accidental spaces and force lowercase) 
clean_username = raw_username.strip().lower()

# 2. Convert text strings into math-ready Integers and Floots
target_lpa = int(raw_target_lpa)
daily_hours = float(raw_daily_hours)

# 3. Convert a text string into a real logical boolean gate
# we check if the matches "True" to assign a real True/False vlue
is_committed = is_committed_input == "True"

# --- STEP 3 : LOGICAL CALCULATION ---
# Calculate total estimated hours over a standard 120-day sprint
total_hours = daily_hours * 120

# --- STEP 4 : PRODUTION OUTPUT PIPELINE ---
print("\n" + "="*50)
print("DATA PIPELINE CLEANING COMPLETE")
print("="*50)
print(f"Cleaned User : @{clean_username}")
print(f"Target Salary : ₹{target_lpa} LPA")
print(f"Daily Commitment : {daily_hours} Hours/Day")
print(f"Total Sprint Time : {total_hours} Hours")
print(f"Pipeline Active : {is_committed}")
print("="*50 + "\n")
