import json
from datetime import datetime

ALERTS_FILE = "/var/ossec/logs/alerts/alerts.json"

def append_fake_alert(description, agent_id):
    try:
        # Try to read existing alerts
        try:
            with open(ALERTS_FILE, "r") as f:
                alerts = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            # If file is empty, missing, or corrupted, start with empty array
            alerts = []

        # Append new alert
        alerts.append({
            "rule": {"description": description},
            "agent": {"id": str(agent_id)},
            "timestamp": datetime.now().isoformat()
        })

        # Write back to file
        with open(ALERTS_FILE, "w") as f:
            json.dump(alerts, f, indent=2)

        print(f"✅ Appended alert: {description}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    # Example: simulate 3 new alerts
    append_fake_alert("Test alert 2", 1001)
    append_fake_alert("Test alert 3", 1002)
    append_fake_alert("Test alert 5", 1003)
