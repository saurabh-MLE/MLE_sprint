candidate_name = "meran sharma"
hours_completed = 1020.0
total_projects_built = 0
has_github_portfolio = False

print("\n" + "*"*50)
print("AUTOMATED PLACEMENT TRACKING ENGINE")
print("="*50)

if hours_completed >= 1000 and total_projects_built >= 5 and has_github_portfolio == True:
    placement_tier = "TIER 1 (₹15+ LPA Product Startups)"
    action_required = "Deploy portfolio to AWS and initiate resume blast"

elif hours_completed >= 500 and total_projects_built >= 2:
    placement_tier = "TIER 2 (₹8-₹12 LPA Mid-Scale Tech)"
    action_required = "Build 3 more end-to-end projects immediately"

else:
    placement_tier = "FOUNDATION STAGE (System Integration)"
    action_required = "Keep coding. Finish basics, build your first 2 projects."

print(f"Candidate Profile : @{candidate_name}")
print(f"Evaluation Result : {placement_tier}")
print(f"Next Action Plan : {action_required}")
print("="*50 + "\n")    
