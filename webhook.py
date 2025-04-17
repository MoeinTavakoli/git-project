import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, jsonify
import os
import json
import yaml

app = Flask(__name__)

def load_json(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"\nFile '{filename}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"\nError decoding JSON file.")
        return []

def save_data(notes, filename):  
    with open(filename, 'w') as f:
        json.dump(notes, f, indent=4)
    with open(filename.replace('.json', '.yaml'), 'w') as f:
        yaml.dump(notes, f)
 

def save_alert(alert):
    labels = alert.get("labels", {})
    team = labels.get("team", "unknown_team")
    severity = labels.get("severity", "unknown_severity")

    dir_path = os.path.join("alerts", team)
    os.makedirs(dir_path, exist_ok=True)

    file_path = os.path.join(dir_path, f"{severity}.json")

    existing_alerts = load_json(file_path)
    existing_alerts.append(alert)

    save_data(existing_alerts, file_path)



def send_email_alert(summary, description):
    SENDER_EMAIL = "mehrabanbaghery368@gmail.com"
    SENDER_PASSWORD = "*************"  # Gmail App Password  #i get this password from app password after activate 2step verifaction
    RECIPIENT_EMAIL = "mhrbnbaghery@gmail.com"

    subject = f"[ALERT] {summary}"
    body = f"{summary}\n\n{description}"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT_EMAIL

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())
        print(" Email sent successfully.")
    except Exception as e:
        print(f" Failed to send email: {e}")



########با این دستورا ایمیل ارسال نشد
# def send_email(subject, body):
#     sender_email = "mehrabanbaghery368@gmail.com"
#     receiver_email = "mhrbnbaghery@gmail.com"
#     password = "*************"  

#     msg = MIMEMultipart()
#     msg['From'] = sender_email
#     msg['To'] = receiver_email
#     msg['Subject'] = subject

#     msg.attach(MIMEText(body, 'plain'))

#     try:
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()  
#         server.login(sender_email, password)
#         text = msg.as_string()
#         server.sendmail(sender_email, receiver_email, text)
#         server.quit()
#         print(f"Email sent to {receiver_email}")
#     except Exception as e:
#         print(f"Error sending email: {str(e)}")

# def print_to_email(alert):
#     labels = alert.get('labels', {})
#     annotations = alert.get('annotations', {})

#     team = labels.get('team', 'unknown_team')
#     severity = labels.get('severity', 'unknown_severity')
#     summary = annotations.get('summary', 'No summary')
#     description = annotations.get('description', 'No description')

#     email_subject = f"New Alert: {severity} - {team}"
#     email_body = f"""
#      New Alert Received:
    
#     Team      : {team}
#     Severity  : {severity}
#     Summary   : {summary}
#     Description:
#     {description}
#     """
    
#     send_email(email_subject, email_body)

def print_to_console(alert):
    labels = alert.get('labels', {})
    annotations = alert.get('annotations', {})

    team = labels.get('team', 'unknown_team')
    severity = labels.get('severity', 'unknown_severity')
    summary = annotations.get('summary', 'No summary')
    description = annotations.get('description', 'No description')

    print(" New Alert Received:")
    print(f"Team      : {team}")
    print(f"Severity  : {severity}")
    print(f"Summary   : {summary}")
    print(f"Description:\n{description}")
    print("=" * 40)

@app.post('/webhook')
def webhook():
    try:
        if request.method != 'POST':
            return jsonify({"error": "Invalid request method, POST expected"}), 405
        
        data = request.get_json(force=True)
        if not data or 'alerts' not in data:
            return jsonify({"error": "Missing 'alerts' in request data"}), 400
        
        alerts = data.get('alerts', [])
        if not isinstance(alerts, list):
            return jsonify({"error": "'alerts' must be a list"}), 400
        
        for alert in alerts:
            if not isinstance(alert, dict):
                return jsonify({"error": "Each alert must be a dictionary"}), 400
            
            summary = alert.get("annotations", {}).get("summary", "No summary")
            description = alert.get("annotations", {}).get("description", "No description")

            save_alert(alert) 
            print_to_console(alert) 
            send_email_alert(summary, description)
            # print_to_email(alert)

        return jsonify({"message": "Alerts processed"}), 200

    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format"}), 400
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
