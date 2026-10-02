3.	# AuraCare Health System Core
4.	APP_VERSION = "2.0.0-Beta"
5.	MODULES_ENABLED = []

def get_doctor_schedule(doctor_name):
    schedule = {
        "Dr. Khan": ["Monday", "Wednesday", "Friday"],
        "Dr. Ahmed": ["Tuesday", "Thursday"],
        "Dr. Ali": ["Monday", "Thursday", "Saturday"],
    }
    return schedule.get(doctor_name, "Doctor not found")
def triage_function(title, description):
    text = (title + " " + description).lower()
    
    # Define keywords for different priority levels
    high_priority_keywords = ["down", "crash", "urgent", "security", "broken"]
    medium_priority_keywords = ["slow", "error", "issue", "fail"]
    
    # Check for high priority
    for word in high_priority_keywords:
        if word in text:
            return {"priority": "High", "action": "Route to Tier 2 Support"}
            
    # Check for medium priority
    for word in medium_priority_keywords:
        if word in text:
            return {"priority": "Medium", "action": "Route to General Queue"}
            
    # Default to low priority
    return {"priority": "Low", "action": "Route to Self-Service / Bot"}

# Example usage
ticket = triage_function("System Crash", "The main production server is down completely.")
print(ticket)
