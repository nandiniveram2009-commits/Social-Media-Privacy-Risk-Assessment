"""
PURPOSE: Extract privacy risk features from raw user questionnaire responses.
"""

def extract_privacy_features(responses: dict) -> dict:
    features = {}
    
    # Profile Visibility
    features['profile_public'] = 1.0 if responses.get('profile_visibility') == 'PUBLIC' else (0.5 if responses.get('profile_visibility') == 'FRIENDS' else 0.0)
    features['search_engine_indexed'] = 1.0 if responses.get('search_engine_visible') == 'YES' else 0.0
    
    # Personal Info Exposure
    features['phone_exposed'] = 1.0 if responses.get('phone_public') == 'YES' else 0.0
    features['email_exposed'] = 1.0 if responses.get('email_public') == 'YES' else 0.0
    features['birthday_exposed'] = 1.0 if responses.get('birthday_public') == 'YES' else 0.0
    features['workplace_exposed'] = 1.0 if responses.get('workplace_public') == 'YES' else 0.0
    
    # Location Privacy
    features['realtime_location'] = 1.0 if responses.get('location_public') == 'YES' else 0.0
    features['travel_broadcasting'] = 1.0 if responses.get('travel_posts') == 'YES' else 0.0
    
    # Account Security
    features['mfa_disabled'] = 1.0 if responses.get('mfa_enabled') == 'NO' else 0.0
    features['password_reuse'] = 1.0 if responses.get('password_reuse_reported') == 'YES' else 0.0
    features['login_alerts_disabled'] = 1.0 if responses.get('login_alerts_enabled') == 'NO' else 0.0
    
    # Social Engineering & Connections
    features['unknown_connections_accepted'] = 1.0 if responses.get('unknown_connections') in ['YES', 'OFTEN', 'SOMETIMES'] else 0.0
    features['tag_review_disabled'] = 1.0 if responses.get('tag_review_enabled') == 'NO' else 0.0
    features['third_party_unreviewed'] = 1.0 if responses.get('third_party_apps_reviewed') == 'NO' else 0.0
    
    return features