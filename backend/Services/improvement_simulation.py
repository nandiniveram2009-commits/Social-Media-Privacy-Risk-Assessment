"""
PURPOSE: Simulate score reduction when applying recommended privacy controls.
"""

def simulate_improvements(current_score: float, implemented_changes: list) -> dict:
    reduction = 0.0
    
    change_impacts = {
        "hide_phone": 12.0,
        "disable_realtime_location": 15.0,
        "enable_mfa": 20.0,
        "restrict_unknown_connections": 10.0,
        "enable_tag_review": 8.0,
        "review_third_party_apps": 5.0
    }
    
    for change in implemented_changes:
        reduction += change_impacts.get(change, 5.0)
        
    simulated_score = max(0.0, round(current_score - reduction, 2))
    
    if simulated_score <= 20: level = "LOW"
    elif simulated_score <= 40: level = "MODERATE"
    elif simulated_score <= 70: level = "HIGH"
    else: level = "CRITICAL"
    
    return {
        "previous_score": current_score,
        "simulated_score": simulated_score,
        "points_reduced": round(current_score - simulated_score, 2),
        "new_risk_level": level,
        "disclaimer": "This is a framework simulation, not a guarantee of real-world security."
    }
