import logging
import logging.handlers
import os
import json
import requests
from functions import *

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)


if __name__ == "__main__":
    TELEGRAM_TOKEN = "5740632861:AAFFDVj4JLqMz9Poss_AZv9cIH7xXCoAVX0"
    CHAT_ID = "593517818"
    message = GetLatestTickersPrice(['TSLA','MSFT'])
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
    print(url)
    r = requests.get(url)