from flask import Flask, jsonify
from importlib import import_module

MODULES = ['cpu', 'memory', 'disk']
app = Flask(__name__)


def get_stats():
    stats = [m.get_stat() for m in __MODULES__]

    return stats


@app.route("/")
def stats():
    return jsonify(get_stats())


# load modules
__MODULES__ = [import_module('modules.{}'.format(m)) for m in MODULES]
