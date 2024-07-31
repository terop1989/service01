import time
import random

from flask import Flask

app = Flask(__name__)
error_codes = ('404', '502')
status_codes = [200, 404]

@app.route('/one')
def route_one():
    time.sleep(random.random() * 0.2)
    return 'Route 1\n'

@app.route('/two')
def route_two():
    time.sleep(random.random() * 0.2)
    return 'Route 2\n'

@app.route('/three')
def route_three():
    time.sleep(random.random() * 0.2)
    return 'Route 3\n'

@app.route('/four')
def route_four():
    time.sleep(random.random() * 0.2)
    return 'Error...\n', random.choice(error_codes)

@app.route('/health')
def health():
  status = random.choice(status_codes)
  logger.info({"message" : "calling root route"})
  return ('Status ' + str(status) + '\n', status)



if __name__ == '__main__':
    app.run('0.0.0.0', 5000, threaded=True)