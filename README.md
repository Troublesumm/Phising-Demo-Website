# Phising-Demo-Website
This is a simple Python Flask Code that demonstrates how phishing websites can collect sensitive user information in seconds.

It is built purely for **ethical, educational, and awareness purposes**, such as cybersecurity training sessions and workshops, to show non-technical users how easily attackers can harvest their personal data.


 Features
. Collects visitor IP address and User-Agent when they open the page.  
. Captures submitted usernames and passwords.  
. Logs all data with timestamps into a local `log.txt` file.  
. Simple HTML login page to mimic a generic login form.

 How it works

- When a user visits the page, their IP and browser details are logged.
- If they submit the login form, their entered username and password are also logged.
- This simulates how real phishing attacks gather credentials and device info.

 Tech Stack:
Python 3 with Flask
HTML/CSS for the frontend

 Usage

> ⚠ For ethical demo use only.  
> Please do not deploy this on any public server without explicit permission.

1. Clone the repository
2. Install dependencies
   ```bash
   pip install flask
