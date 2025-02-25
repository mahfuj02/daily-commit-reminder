import requests
from datetime import datetime, timedelta
import os

# Replace with your GitHub username and repository
USERNAME = 'mahfuj02'
REPO = 'daily-commit-reminder'
TOKEN = os.getenv('GITHUB_TOKEN')  # Get the token from environment variable

def get_commits():
    url = f'https://api.github.com/repos/{USERNAME}/{REPO}/commits'
    headers = {'Authorization': f'token {TOKEN}'}
    response = requests.get(url, headers=headers)
    return response.json()

def check_commits_today():
    commits = get_commits()
    today = datetime.utcnow().date()
    
    for commit in commits:
        commit_date = datetime.strptime(commit['commit']['author']['date'], '%Y-%m-%dT%H:%M:%SZ').date()
        if commit_date == today:
            return True
    return False

def main():
    if check_commits_today():
        print("You have committed today.")
    else:
        print("You haven't committed today. Please commit something!")

if __name__ == "__main__":
    main()
