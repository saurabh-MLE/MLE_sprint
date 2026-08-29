class Candidate:
    def __init__(self, name, hours, projects, github_active):
        self.name = name
        self.hours = hours
        self.projects = projects
        self.github_active = github_active

    def evaluate_profile(self):
        
        if self.hours >= 1000 and self.projects >= 5 and self.github_active == True:
            return "TIER 1 (₹15+ LPA Direct Screening)"  
        else:
            return "FOUNDATION STAGE (Keep Building)"   

if __name__ == "__main__":
    print("\n" + "="*50)
    print("OBJECT-ORIENTED PLACEMENT SYSTEM ACTIVE")
    print("="*50)
    
    candidate_1 = Candidate("Saurabh", 1020, 5, True)
    tier_result = candidate_1.evaluate_profile()
    
    print(f"Candidate Name : {candidate_1.name}")
    print(f"Logged Hours   : {candidate_1.hours} Hours")
    print(f"Final Outcome  : {tier_result}")
    print("="*50 + "\n")
