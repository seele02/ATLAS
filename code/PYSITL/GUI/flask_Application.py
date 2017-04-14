from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from werkzeug.exceptions import abort
import json

app = Flask(__name__)


class Node:
    def __init__(self, name, num, lat, lng):
        self.name = name
        self.lat = lat
        self.long = lng
        self.num = num
        self.key = str(num)
        print self.key


Nodes = {
    Node("(Sample) Temp Node", 1, 51.8856654, -8.5466063),
    Node("(Sample) Humidity Node", 2, 51.8859336, -8.5495246),
}
nodes_by_num = {Node.key: Node for Node in Nodes}


@app.route('/')
def index():
    return render_template('index.html', Nodes=Nodes)

@app.route('/<node_num>')
def show_node(node_num):
    MyNode = nodes_by_num.get(node_num)
    print MyNode

    if Node:
        return render_template('map.html', Node=MyNode)
    else:
        abort(404)
    return '<h2>Tuna is good</h2>'


@app.route('/map')
def map():
    return '<h2>Tuna is good</h2>'


if __name__ == "__main__":
    app.run()
