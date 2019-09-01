from flask import Flask, render_template
from gevent.pywsgi import WSGIServer

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    #app.run(host='127.0.0.1', port=5000, debug=True)
    # Serve the app with gevent
    print('server is runing on localhost:5000')
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()