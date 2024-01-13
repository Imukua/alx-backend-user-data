#!/usr/bin/env python3
"""logger file func"""


import logging
from typing import List
import re

def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
        """
        Filters the data and reducts certain words
        """
        for val in fields:
             message = re.sub(f"{val}=.*?{separator}",
                              f"{val}={redaction}{separator}", message)
        return message
