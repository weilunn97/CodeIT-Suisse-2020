import logging
import socket

from flask import request, jsonify, Flask

from codeitsuisse.routes.cluster import cluster
from codeitsuisse.routes.contact_trace import contact_trace
from codeitsuisse.routes.inventory_management import inventory_management
from codeitsuisse.routes.salad_spree import salad_spree

app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route('/', methods=['GET'])
def default_route():
    return "Python Template"


@app.route('/salad-spree', methods=['POST'])
def evaluate_salad_spree():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    n, arrs = data.get("number_of_salads"), data.get("salad_prices_street_map")
    result = salad_spree(n, arrs)
    logging.info("My result :{}".format(result))
    return jsonify(result=result)


@app.route('/contact_trace', methods=['POST'])
def evaluate_contact_trace():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    n, arrs = data.get("number_of_salads"), data.get("salad_prices_street_map")
    result = contact_trace(n, arrs)
    logging.info("My result :{}".format(result))
    return jsonify(result=result)


@app.route('/inventory-management', methods=['POST'])
def evaluate_inventory_management():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    name, items = data[0].get("searchItemName"), data[0].get("items")
    result = inventory_management(name, items)
    logging.info("My result :{}".format(result))
    return jsonify(result)


@app.route('/cluster', methods=['POST'])
def evaluate_cluster():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    result = cluster(data)
    logging.info("My result :{}".format(result))
    return jsonify(answer=result)


logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

if __name__ == "__main__":
    logging.info("Starting application ...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 0))
    port = sock.getsockname()[1]
    sock.close()
    app.run(port=5000)
