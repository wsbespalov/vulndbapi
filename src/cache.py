import os
from diskcache import Cache as DC
from io import BytesIO


class Cache(object):

    def __init__(self):
        try:
            self.cache = DC('./tmp')
        except Exception as ex:
            print('Get an exception with diskcache open: {}'.format(ex))
            self.cache = None

    def __del__(self):
        try:
            self.cache.close()
        except Exception as ex:
            print('Get an exception with diskcache close: {}'.format(ex))

    def set(self, key, value):
        if self.cache is not None:
            self.cache.set(key, BytesIO(value), read=True, tag=u'data')

    def get(self, key):
        if self.cache is not None:
            value = self.cache.get(key, default=b'', read=True, tag=True)
            if value is not None and value != b'':
                return value
        return None

    def pop(self, key):
        if self.cache is not None:
            value = self.cache.pop(key, default=b'', read=True, tag=True)
            if value is not None and value != b'':
                return value
        return None

    def delete(self, key):
        if self.cache is not None:
            self.cache.delete(key)

    def create_index(self):
        if self.cache is not None:
            self.cache.create_tag_index()
            return self.cache.tag_index
        return None

    def clear_all(self):
        if self.cache is not None:
            self.cache.clear()
