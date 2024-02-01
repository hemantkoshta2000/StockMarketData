import requests

def send_push_notification(title, body):
    url = 'https://api.pushbullet.com/v2/pushes'
    headers = {
        'Access-Token': 'o.oQOwBggOmqZIuwhD6lymmiwDQpoDrGyM',
        'Content-Type': 'application/json'
    }
    data = {
        'type': 'note',
        'title': title,
        'body': body
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Notification sent successfully.")
    else:
        print("Failed to send notification. Status code:", response.status_code)
        print(response.text)

# Replace 'YOUR_API_KEY' with your actual Pushbullet API key
# title = 'Notification Title'
# body = 'Notification Body'

# send_push_notification(title, body)