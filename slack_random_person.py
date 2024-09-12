import random
import os
import json
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Your Slack API token
slack_token = os.getenv("SLACK_TOKEN")
not_relevant = ['Amir Amer', 'Aviv Golan', 'Gal Alon', 'Slackbot']
index_file = "current_index.json"

# Initialize the Slack client
client = WebClient(token=slack_token)

def get_team_members():
    try:
        # Retrieve the list of users in the workspace
        response = client.users_list()
        users = response['members']
        
        # Filter out bots and deactivated users
        members = [user for user in users if not user['is_bot'] and user['deleted'] == False and user['real_name'] not in not_relevant]
        return members
    
    except SlackApiError as e:
        print(f"Error fetching users: {e.response['error']}")
        return []

def send_message_to_user(user_id, message):
    try:
        # Send a direct message to the selected user
        client.chat_postMessage(channel=user_id, text=message)
        print(f"Message sent to {user_id}")
        
    except SlackApiError as e:
        print(f"Error sending message: {e.response['error']}")

def load_index():
    if os.path.exists(index_file):
        with open(index_file, "r") as f:
            return json.load(f)["index"]
    return 0  # Start from the beginning if the file doesn't exist

def save_index(index):
    with open(index_file, "w") as f:
        json.dump({"index": index}, f)

def main():
    members = get_team_members()
    if not members:
        print("No members available to send a message.")
        return
    
    # Load the current index
    current_index = load_index()

    # Ensure the index is within the bounds of the members list
    if current_index >= len(members):
        current_index = 0  # Reset to the beginning if we've reached the end

    selected_member = members[current_index]
    user_id = selected_member['id']
    user_name = selected_member['real_name']

    # Customize your message here
    message = f"Hello {user_name}, you are the tin man today!"
    
    admin_user_id_list = ["U06MCDP1679", "U06MVF8087N"]  # Yaniv, David
    admin_message = f"{user_name} has been selected as the tin man today."
    
    for admin_user_id in admin_user_id_list:
        send_message_to_user(admin_user_id, admin_message)
    
    # Send the message to the selected user
    send_message_to_user(user_id, message)

    # Increment and save the next index
    current_index = (current_index + 1) % len(members)
    save_index(current_index)

if __name__ == "__main__":
    main()
