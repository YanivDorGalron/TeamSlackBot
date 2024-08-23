# 🎩 Tin Man Slack Bot

This Python script randomly selects a team member from a Slack workspace and assigns them as the "Tin Man" for the day, notifying them via a direct message on Slack. It also sends a notification to specified admins about the selected "Tin Man".

## 🌟 Features

-   **🔍 Fetch Team Members:** Retrieves the list of active members in the Slack workspace.
-   **🚫 Exclusions:** Filters out bots, deactivated users, and a predefined list of irrelevant members.
-   **🎲 Random Selection:** Randomly selects one active member.
-   **💬 Messaging:** Sends a customized direct message to the selected member, as well as a notification to the admins.

## 🛠️ Prerequisites

-   🐍 Python 3.6+
-   🔐 Slack API token with the necessary permissions to read user information and send messages.

## 📝 Setup

1.  **📂 Clone the repository:**
    
    `git clone <repository_url>
    cd <repository_directory>` 
    
2.  **📦 Install required Python packages:**
    
    `pip install slack-sdk` 
    
3.  **🔧 Set up your Slack API token:**
    
    Ensure that your Slack API token is stored as an environment variable. You can set it up in your shell configuration file (e.g., `.bashrc`, `.zshrc`):
        
    `export SLACK_TOKEN='your-slack-token'` 
    
    Replace `'your-slack-token'` with your actual Slack API token.
    

4.  **🛠️ Customize the script:**
    -   Update the `not_relevant` list with the names of any team members who should be excluded from the random selection.
    -   Update the `admin_user_id_list` with the Slack user IDs of the admins who should be notified.


## 🚀 Usage

To run the script:

`python tin_man.py` 

This will:


1.  🧑‍🤝‍🧑 Retrieve the list of active members in the Slack workspace.
2.  🎲 Randomly select a member from the list (excluding bots, deactivated users, and any users in the `not_relevant` list).
3.  📩 Send a direct message to the selected member informing them that they are the "Tin Man" for the day.
4.  📢 Notify the specified admins about the selected member.

## ⏰ Automating with `crontab -e`

To automate the execution of the Tin Man Slack Bot script at regular intervals, such as every day at a specific time, you can use the `cron` job scheduler on Unix-like systems. The `crontab -e` command allows you to edit the cron jobs for the current user.

### Steps to Schedule the Script

1.  **🖊️ Open the Crontab File:**
    
    To open the crontab file for editing, run the following command in your terminal:
   
    `crontab -e` 
    
    This command opens the user's cron table in a text editor, allowing you to add or modify cron jobs.
    
2.  **➕ Add a New Cron Job:**
    
    To schedule the Tin Man Slack Bot script to run at a specific time, add a new line in the crontab file with the following format:
   
    `minute hour day month day_of_week /path/to/python /path/to/tin_man.py` 
    
    For example, to run the script every day at 9:00 AM, you would add:
    
    `0 9 * * * /usr/bin/python3 /path/to/tin_man.py` 
    
    -   `0 9 * * *` specifies that the script should run every day at 9:00 AM.
    -   Replace `/usr/bin/python3` with the path to your Python interpreter.
    -   Replace `/path/to/tin_man.py` with the full path to the `tin_man.py` script.

3.  **💾 Save and Exit:**
    
    After adding the cron job, save the file and exit the editor. The new cron job is now scheduled and will run automatically at the specified time.
    

## 🛡️ Error Handling

The script handles errors related to fetching users or sending messages from Slack. If an error occurs, the script will print an error message to the console.

## 📜 License

This project is licensed under the MIT License.