"""
PURPOSE: Compute category-wise and overall weighted privacy risk scores (0-100).
"""

def calculate_category_scores(features: dict) -> dict:
    scores = {}
    
    # Profile Visibility Score (0-100)
    scores['Profile Visibility'] = min(100.0, (features.get('profile_public', 0) * 70 + features.get('search_engine_indexed', 0) * 30))
    
    # Personal Information Score
    scores['Personal Information'] = min(100.0, (
        features.get('phone_exposed', 0) * 35 +
        features.get('email_exposed', 0) * 25 +
        features.get('birthday_exposed', 0) * 25 +
        features.get('workplace_exposed', 0) * 15
    ))
    
    # Location Exposure Score
    scores['Location Privacy'] = min(100.0, (features.get('realtime_location', 0) * 60 + features.get('travel_broadcasting', 0) * 40))
    
    # Account Security Score
    scores['Account Security'] = min(100.0, (
        features.get('mfa_disabled', 0) * 50 +
        features.get('password_reuse', 0) * 30 +
        features.get('login_alerts_disabled', 0) * 20
    ))
    
    # Social Engineering Score
    scores['Social Engineering'] = min(100.0, (features.get('unknown_connections_accepted', 0) * 100))
    
    # Tagging & Third-Party Apps
    scores['Tagging Risk'] = 100.0 if features.get('tag_review_disabled', 0) == 1.0 else 10.0
    scores['Third-Party Apps'] = 100.0 if features.get('third_party_unreviewed', 0) == 1.0 else 10.0
    
    # Default padding for other categories
    for cat in ['Posts & Content', 'Digital Footprint', 'Content Exposure']:
        if cat not in scores:
            scores[cat] = 40.0
            
    return scores

def calculate_overall_risk(category_scores: dict) -> tuple:
    weights = {
        'Profile Visibility': 0.10,
        'Personal Information': 0.15,
        'Location Privacy': 0.15,
        'Posts & Content': 0.05,
        'Tagging Risk': 0.05,
        'Account Security': 0.20,
        'Third-Party Apps': 0.05,
        'Social Engineering': 0.15,
        'Digital Footprint': 0.10
    }
    
    total_score = 0.0
    total_weight = 0.0
    
    for cat, weight in weights.items():
        score = category_scores.get(cat, 50.0)
        total_score += score * weight
        total_weight += weight
        
    overall = round(total_score / total_weight, 2) if total_weight > 0 else 0.0
    
    if overall <= 20: level = "LOW"
    elif overall <= 40: level = "MODERATE"
    elif overall <= 70: level = "HIGH"
    else: level = "CRITICAL"
    
    return overall, level
