"""
Context manager for saving object
"""
from contextlib import contextmanager


@contextmanager
def object_saver(obj):
    yield obj
    obj.save()
