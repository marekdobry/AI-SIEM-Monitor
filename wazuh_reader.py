import json

def get_wazuh_alerts(log_file="/var/ossec/logs/alerts/alerts.json"):
    alerts = []
    try:
        with open(log_file, 'r') as f:
            for line in f:
                try:
                    data = json.loads(line.strip())
                    alerts.append(data)
                except json.JSONDecodeError:
                    continue
    except FileNotFoundError:
        print(f"Log file not found: {log_file}")
    return alerts
