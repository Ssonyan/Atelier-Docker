from flask import Flask, jsonify
from flask_cors import CORS
import os
from datetime import datetime
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)
CORS(app)

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv('DB_HOST', 'postgres'),
        database=os.getenv('DB_NAME', 'myapp'),
        user=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASSWORD', 'postgres')
    )

@app.route('/api/health')
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/db-test')
def db_test():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT version();')
    version = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify(version)

@app.route('/api/system-check')
def system_check():
    # Test database connection
    try:
        conn = get_db_connection()
        db_status = "connected"
        conn.close()
    except Exception as e:
        db_status = f"error: {str(e)}"

    return jsonify({
        "service": "flask",
        "status": "ok",
        "timestamp": datetime.now().isoformat(),
        "database": db_status,
        "environment": {
            "FLASK_ENV": os.getenv("FLASK_ENV"),
            "DB_HOST": os.getenv("DB_HOST"),
            "DB_NAME": os.getenv("DB_NAME")
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)