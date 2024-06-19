import logging
import os
from datetime import datetime
from from_root import from_root

LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%S')}.log"
log_path = os.path.join(from_root(), "log", LOG_FILE)

os.makedirs(log_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[ %(asctime)s ] - %(name)s - %(levelname)s - %(message)s",
)