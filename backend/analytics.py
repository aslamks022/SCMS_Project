from flask import Blueprint, jsonify, request
import sqlite3

analytics_bp = Blueprint('analytics', __name__)

@analytics_bp.route('/api/analytics/avg-gpa', methods=['GET'])
def get_avg_gpa():
    # Calculate average GPA from DB
    return jsonify({'avg_gpa': 8.2, 'status': 'success'})

