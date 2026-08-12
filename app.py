import time
import random
from flask import Flask, Response, render_template

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    # Serves the index.html page
    return render_template('index.html')

@app.route('/stream-data')
def stream_data():
    def generate_numbers():
        while True:
            # Generate random integer between 1 and 10
            number = random.randint(1, 10)
            
            # Send number as a Server-Sent Event (SSE)
            yield f"data: {number}\n\n"
            time.sleep(1)  # Delay 1 second

    return Response(generate_numbers(), mimetype='text/event-stream')

if __name__ == '__main__':
    # Install Flask first if needed: pip install flask
    print("Starting Flask server at http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
