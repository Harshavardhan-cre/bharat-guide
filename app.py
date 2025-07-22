from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('result.html')

@app.route('/filter', methods=['POST'])
def filter_schemes():
    # Logic will go here
    return "Schemes coming soon"

if __name__ == '__main__':
    app.run(debug=True)
