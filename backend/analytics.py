from flask import Blueprint, jsonify, request
import sqlite3

analytics_bp = Blueprint('analytics', __name__)
