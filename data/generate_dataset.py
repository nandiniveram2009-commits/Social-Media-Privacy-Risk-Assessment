import os
import random
import csv

def generate_synthetic_dataset(num_records=1000):
    os.makedirs("data", exist_ok=True)
    file_path = "data/social_media_privacy_assessments.csv"
    
    visibility_options = ["PUBLIC", "FRIENDS", "PRIVATE"]
    binary_options = ["YES", "NO"]
    frequency_options = ["OFTEN", "SOMETIMES", "RARELY", "NEVER"]
    
    headers = [
        "profile_id", "profile_visibility", "phone_public", "email_public",
        "birthday_public", "location_public", "workplace_public", "education_public",
        "relationship_public", "posts_public", "location_tagging", "travel_posts",
        "unknown_connections", "tag_review_enabled", "third_party_apps_reviewed",
        "mfa_enabled", "login_alerts_enabled", "password_reuse_reported",
        "suspicious_link_awareness", "old_posts_reviewed", "privacy_settings_reviewed",
        "risk_score", "risk_level"
    ]
    
    rows = []
    for i in range(1, num_records + 1):
        p_vis = random.choice(visibility_options)
        phone = random.choice(binary_options)
        email = random.choice(binary_options)
        bday = random.choice(binary_options)
        loc = random.choice(binary_options)
        work = random.choice(binary_options)
        edu = random.choice(binary_options)
        rel = random.choice(binary_options)
        posts = random.choice(visibility_options)
        loc_tag = random.choice(binary_options)
        travel = random.choice(binary_options)
        unknown_conn = random.choice(frequency_options)
        tag_rev = random.choice(binary_options)
        app_rev = random.choice(binary_options)
        mfa = random.choice(binary_options)
        alerts = random.choice(binary_options)
        pw_reuse = random.choice(binary_options)
        link_aware = random.choice(frequency_options)
        old_posts = random.choice(binary_options)
        settings_rev = random.choice(binary_options)
        
        # Calculate heuristic synthetic risk score (0-100)
        score = 20
        if p_vis == "PUBLIC": score += 15
        if phone == "YES": score += 10
        if email == "YES": score += 8
        if bday == "YES": score += 7
        if loc == "YES": score += 10
        if travel == "YES": score += 8
        if unknown_conn in ["OFTEN", "SOMETIMES"]: score += 10
        if tag_rev == "NO": score += 5
        if mfa == "NO": score += 15
        if pw_reuse == "YES": score += 10
        if app_rev == "NO": score += 5
        
        score = min(max(score + random.randint(-10, 10), 0), 100)
        
        if score <= 20: level = "LOW"
        elif score <= 40: level = "MODERATE"
        elif score <= 70: level = "HIGH"
        else: level = "CRITICAL"
        
        rows.append([
            f"SYNTH_USER_{i:04d}", p_vis, phone, email, bday, loc, work, edu,
            rel, posts, loc_tag, travel, unknown_conn, tag_rev, app_rev,
            mfa, alerts, pw_reuse, link_aware, old_posts, settings_rev,
            score, level
        ])
        
    with open(file_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
        
    print(f"[+] Successfully generated {num_records} synthetic records at {file_path}")

if __name__ == "__main__":
    generate_synthetic_dataset()
