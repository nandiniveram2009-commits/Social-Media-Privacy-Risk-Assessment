"""
PURPOSE: Generate actionable, personalized security recommendations.
"""

def generate_recommendations(findings: list) -> list:
    recommendations = []
    
    for finding in findings:
        sev = finding['severity']
        priority = "IMMEDIATE" if sev == "CRITICAL" else ("IMPORTANT" if sev == "HIGH" else "GOOD PRACTICE")
        
        if "phone number" in finding['finding'].lower():
            rec = "Navigate to account privacy settings and restrict phone number visibility to 'Only Me'."
        elif "location" in finding['finding'].lower():
            rec = "Disable real-time location tagging on posts and refrain from checking in at sensitive locations."
        elif "mfa" in finding['finding'].lower():
            rec = "Enable Multi-Factor Authentication immediately using an authenticator app or hardware security key."
        elif "unknown connections" in finding['finding'].lower():
            rec = "Adopt a strict connection policy: verify mutual acquaintances or real-world identity before accepting requests."
        elif "tag review" in finding['finding'].lower():
            rec = "Enable manual tag review so tagged posts require your explicit approval before appearing on your profile."
        else:
            rec = "Review privacy controls and adhere to the principle of least privilege."
            
        recommendations.append({
            "finding": finding['finding'],
            "priority": priority,
            "recommendation": rec
        })
        
    return recommendations
