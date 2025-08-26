import logging

logger = logging.getLogger("qa_logger")
logger.setLevel(logging.DEBUG)  # DEBUG supaya semua step dicatat

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", "%H:%M:%S")

ch = logging.StreamHandler()  # supaya muncul di console
ch.setFormatter(formatter)
logger.addHandler(ch)