from wazuh_reader import get_wazuh_alerts
from ai_model import classify_alert
from ticket_manager import create_ticket
import json
import os

# File to store processed alert IDs
PROCESSED_FILE = "processed_alerts.json"

# Load processed alert IDs if it exists
if os.path.exists(PROCESSED_FILE):
    with open(PROCESSED_FILE, "r") as f:
        processed_alerts = set(json.load(f))
else:
    processed_alerts = set()

def get_alert_id(alert):
    """
    Return a unique identifier for an alert.
    Use 'id' if available; else combine timestamp + description.
    """
    alert_id = alert.get("id")
    if not alert_id:
        ts = alert.get("timestamp", "")
        description = alert.get("rule", {}).get("description", "")
        alert_id = f"{ts}-{description}"
    return alert_id

def main():
    alerts = get_wazuh_alerts("/var/ossec/logs/alerts/alerts.json")
    if not alerts:
        print("No alerts found.")
        return

    # Filter only new alerts
    new_alerts = [a for a in alerts if get_alert_id(a) not in processed_alerts]

    if not new_alerts:
        print("No new alerts to process.")
        return

    print(f"Loaded {len(alerts)} alerts. Processing {len(new_alerts)} new alerts...\n")

    for alert in new_alerts[:20]:  # Process first 20 for demo
        description = alert.get("rule", {}).get("description", "No description available")
        severity = classify_alert(description)
        print(f"[{severity}] {description}")

        if severity == "HIGH":
            create_ticket(alert)

        # Add alert ID to processed set
        processed_alerts.add(get_alert_id(alert))

    # Save processed alert IDs to file
    with open(PROCESSED_FILE, "w") as f:
        json.dump(list(processed_alerts), f)

if __name__ == "__main__":
    main()