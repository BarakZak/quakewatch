import os
from flask import Flask
import logging

app = Flask(__name__)

# Read environment variables
env = os.getenv("ENV", "development")
log_level = os.getenv("LOG_LEVEL", "INFO").upper()
db_password = os.getenv("DB_PASSWORD", "default-password")

# Set up logging
try:
    os.makedirs("/app/logs", exist_ok=True)  # Ensure /app/logs exists
    logging.basicConfig(
        filename='/app/logs/app.log',
        level=getattr(logging, log_level, logging.INFO),
        format='%(asctime)s - %(message)s',
        filemode='a'
    )
except Exception as e:
    print(f"Failed to configure logging: {e}")
    logging.basicConfig(
        level=getattr(logging, log_level, logging.INFO),
        format='%(asctime)s - %(message)s'
    )

@app.route('/')
def hello():
    logging.info(f"Homepage visited in {env} mode!")
    return f"QuakeWatch: Welcome to Earthquake Monitoring! Running in {env}"

@app.route('/health')
def health():
    logging.debug("Health check OK")
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)