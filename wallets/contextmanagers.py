"""
Context manager for saving object
"""
from contextlib import contextmanager


@contextmanager
def object_saver(obj):
    try:
        _obj = obj
        yield _obj
    finally:
        _obj.save()
