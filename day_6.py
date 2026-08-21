candidates_batch = [
    {
        "name" : "Saurabh",
        "hours_logged" : 1020,
        "projects_count" : 5,
        "github_active" : True
     },
     {
          "name" : "Rahul",
          "hours_logged" : 450,
          "projects_count" : 1,
          "github_active" : False
     },
     {
          "name" : "Amit",
          "hours_logged" : 1200,
          "projects_count" : 2,
          "github_active" : True
     }
]

print("\n" + "="*50)
print("BATCH EVALUATION PIPELINE : TIER 1 MATCHING ENGINE")
print("="*50)

interview_shortlist = []

for candidate in candidates_batch:
    print(f"Analyzing Metrics for : {candidate['name']}...")

    hours = candidate["hours_logged"]
    projects = candidate["projects_count"]
    github = candidate["github_active"]

    if hours >= 1000 and projects >= 5 and github == True:
        status = "MATCH FOUND : ROUTED TO DIRECT SCREENING"
        interview_shortlist.append(candidate["name"])
    else:
        status = "HOLD : CRITERIA UNMET"    

    print(f"Result : {status}\n")

print("="*50)
print(f"PIPELINE RUN COMPLETE. TOTAL INTERVIEWS TRACKED : {len(interview_shortlist)}")
print(f"SHORTLISTED TALENT POOL : {interview_shortlist}")
print("="*50 + "\n")
