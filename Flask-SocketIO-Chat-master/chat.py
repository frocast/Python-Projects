#!/bin/env python
from app import create_app
from flask_socketio import socketio
app = create_app(debug=True)

if __name__ == '__main__':
    socketio.run(app)
