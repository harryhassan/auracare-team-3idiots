3.	# AuraCare Health System Core
4.	APP_VERSION = "1.0.0"
5.	MODULES_ENABLED = []

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
