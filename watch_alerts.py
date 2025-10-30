import json
import time
from ai_model import classify_alert
from ticket_manager import create_ticket

ALERTS_FILE = "/var/ossec/logs/alerts/alerts.json"
processed_alerts = set()

def load_alerts():
    try:
        with open(ALERTS_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def watch_alerts():
    print(f"👀 Watching {ALERTS_FILE} for new alerts...")
    while True:
        alerts = load_alerts()
        new_alerts = []

        for alert in alerts:
            alert_id = (alert.get('timestamp'), alert.get('rule', {}).get('description'))
            if alert_id not in processed_alerts:
                processed_alerts.add(alert_id)
                new_alerts.append(alert)

        if new_alerts:
            print(f"📢 Processing {len(new_alerts)} new alerts...")
            for alert in new_alerts:
                description = alert.get('rule', {}).get('description', 'No description available')
                severity = classify_alert(description)
                print(f"[{severity}] {description}")
                if severity == "HIGH":
                    create_ticket(alert)

        time.sleep(2)

if __name__ == "__main__":
    watch_alerts()