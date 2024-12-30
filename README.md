## Reddit-Parser
Python-based program for parsing through selected subreddits using keywords as filters.

# How to Retrieve Your Reddit Client ID and Secret
To use this project, you’ll need to set up a Reddit application to get your Client ID, Client Secret, and User Agent. Follow the steps below:

Step 1: Log In to Reddit
  Go to https://www.reddit.com/ and log in to your Reddit account. Ensure you are logged in with the account you want to use to access the Reddit API.

Step 2: Navigate to the Developer Portal
  Go to the Reddit developer portal at https://www.reddit.com/prefs/apps. Scroll to the bottom of the page where you’ll see the Developed Applications section.

Step 3: Create a New Application
  Click on the "Create App" or "Create Another App" button. Fill out the form with the following details:
    -Name: Enter a name for your application (e.g., CryptoDataFetcher).
    -App Type: Choose script.
    -Redirect URI: Enter http://localhost:8080 (or any dummy URL if you're not using OAuth for callbacks).
    -Description: Optionally, add a description for your application.
  Click "Create App" to save your application.
  
Step 4: Retrieve Your Credentials
  Once the app is created, you’ll see the following information:

    -Client ID: This is the string directly under the app name.
    -Client Secret: This is the string labeled secret.
    -User Agent: Create your own user agent string. It should be a short description of your app, like script:CryptoDataFetcher:v1.0 (by /u/yourusername).

# Setup Instructions

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

2. Install Dependencies
  pip install -r requirements.txt

3. Create new .env file in project root
   REDDIT_CLIENT_ID=your_client_id
  REDDIT_CLIENT_SECRET=your_client_secret


  REDDIT_USER_AGENT=your_user_agent

5. Run script
   python reddit_parse.py

# Additional Notes
  -Do not share your Client ID and Secret publicly. These should remain private and only be used for your application.
  -If your credentials are exposed, you can regenerate a new Client Secret by editing your application on the Reddit Developer Portal.


