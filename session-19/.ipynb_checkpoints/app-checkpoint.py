from flask import Flask, request, render_template
app = Flask(__name__)
 
@app.route("/", methods=['GET'])
def hello():
    return render_template('echo.html')

@app.route("/echo", methods=['POST'])
def echo(): 
    email = request.form['email']
    return render_template('echo.html', email=email)

app.run(debug=True, port = 5000)