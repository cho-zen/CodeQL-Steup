from flask import Flask, request, render_template

a = "200"
b = "300"

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)

