"""
PURPOSE: Generate prioritized security findings and weaknesses from extracted features.
"""

def generate_privacy_findings(features: dict) -> list:
    findings = []
    
    if features.get('phone_exposed', 0) == 1.0:
        findings.append({
            "category": "Personal Information",
            "finding": "Phone number is publicly visible",
            "severity": "HIGH",
            "description": "Exposing your direct phone number increases risk of targeted SMS phishing (smishing) and automated harvesting."
        })
        
    if features.get('realtime_location', 0) == 1.0:
        findings.append({
            "category": "Location Privacy",
            "finding": "Real-time location sharing enabled",
            "severity": "CRITICAL",
            "description": "Broadcasting real-time whereabouts allows physical tracking, stalking, and monitoring of home vacancy."
        })
        
    if features.get('mfa_disabled', 0) == 1.0:
        findings.append({
            "category": "Account Security",
            "finding": "Multi-Factor Authentication (MFA) is disabled",
            "severity": "CRITICAL",
            "description": "Accounts lacking MFA are extremely vulnerable to credential stuffing, password spraying, and total takeover."
        })
        
    if features.get('unknown_connections_accepted', 0) == 1.0:
        findings.append({
            "category": "Social Engineering",
            "finding": "Accepts connection requests from unknown entities",
            "severity": "HIGH",
            "description": "Unverified connections expand your attack surface for reconnaissance and direct social-engineering payloads."
        })
        
    if features.get('tag_review_disabled', 0) == 1.0:
        findings.append({
            "category": "Tagging Risk",
            "finding": "Tag review permissions disabled",
            "severity": "MODERATE",
            "description": "External users can automatically associate your profile with untrusted photos, locations, or external narratives."
        })
        
    return findings