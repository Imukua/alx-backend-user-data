#!/usr/bin/env python3


import logging
from typing import List
import re

def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
        """
        Filters the data and reducts certain words
        """
        for val in fields:
             message = re.sub(f"{val}=*?{separator}",
                              f"{redaction}{separator}", message)
        return message

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError
