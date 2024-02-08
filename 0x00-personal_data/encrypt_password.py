#!/usr/bin/env python3
"""
Password Encryption using bcrypt
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
        Generates salted and hashed password.
        """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
        Validates whether the provided password matches  hashed password
        """
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        valid = True
    return valid
