from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Welcome to Syndex</h1>
    <p>Your academic workload, organized and managed efficiently.</p>
    """
if __name__ == '__main__':
    app.run()