import py_eureka_client.eureka_client as eureka_client
import os
import socket
import argparse
from flask import Flask


app = Flask(__name__)

ip = socket.gethostbyname(socket.gethostname())
# The flowing code will register your server to eureka server and also start to send heartbeat every 30 seconds
eureka_client.init(eureka_server=os.environ.get('REMOTE'),
                   app_name=os.environ.get('APP_NAME'),
                   instance_ip=os.environ.get('HOST'),
                   renewal_interval_in_secs=int(os.environ.get('RENEWAL_INTERVAL', 5)),
                   duration_in_secs=int(os.environ.get('DURATION_SECONDS', 20)),
                   instance_port=int(os.environ.get('PORT_EUREKA', 8000)))

# Shut down the Eureka client when the application exits
@app.before_first_request
def init_eureka_client():
    def shutdown():
        eureka_client.stop()

if __name__ == '__main__':
    app.run()