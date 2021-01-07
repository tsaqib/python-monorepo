from datetime import datetime
from common.utils.formatter import fmt_message


def ping():
    return fmt_message("Service1", str(datetime.now()))
