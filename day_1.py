import sys
import os

def run_workspace_diagnostics():
    #1 Print a clean professional header block
    print("\n" + "="*50)
    print("TARGET 15+ LPA: DEPLOYMENT DISCIPLINE INITIATED")
    print("="*50 + "n")

    #2 Extract and format core system variable configuration
    python_engine = sys.version.split()[0]
    workspace_path = os.getcwd()

    print(f"[SYSTEM LOG] Active Engine : Python v{python_engine}")
    print(f"[SYSTEN LOG] Current Root  : {workspace_path}") 

    #3 Read the enviorment filedirectory array
    workspace_files = os.listdir('.')
    print(f"[SYSTEM LOG] Project Files : {workspace_files}")

    study_hours_per_day = 8
    total_sprint_days = 120
    total_hours_invested = study_hours_per_day * total_sprint_days

    print(f"[METRIC LOG] Total planned coding investment : {total_hours_invested} Hours")

    print("\n" + "="*50)
    print("STATUS: ENVIORMENT FULLY OPERATIONAL, DAY 1 COMMEND.")
    print("="*50 + "\n")

# Execute the diagonstic controler routing
if __name__ == "__main__":
    run_workspace_diagnostics()

