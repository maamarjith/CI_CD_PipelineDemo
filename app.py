from flask import Flask, render_template, request

app = Flask(__name__)

def validate_password(password):
    if len(password) < 6:
        return "Password must be at least 6 characters"
    if not any(char.isdigit() for char in password):
        return "Password must contain a number"
    return "Valid"

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        validation = validate_password(password)

        if validation == "Valid" and username == "admin":
            message = "Login Successful"
        else:
            message = validation

    return render_template('login.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
