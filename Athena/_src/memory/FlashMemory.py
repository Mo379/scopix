import redis
import numpy as np
from _src.config import FlashMemoryConfig


class _FlashMemory():
    def __init__(self):
        # Create a connection to Vector DB
        self.broker = redis.Redis(
                host='0.0.0.0',
                port=6379,
                db=0
            )

    def _delete(self, key):
        """delete the given key from memory"""
        pass

    def _update(self, key, new_value):
        """updates the value of the key"""
        return self.broker.set(key, new_value)

    def _read(self, key):
        """Reads the value of the key and returns it"""
        return self.broker.get(key)

    def _create(self, key, val):
        """create a key and value pair into redis"""
        return self.broker.mset({key: val})

    def _create_collections(self):
        """ A helper function that creates all collections used by athena

        loops through the hardcoded list of collection names, checks if they
        exist in the vector DB and creates them using a function defined
        in the CrystalMemoryConfig file.
        """
        pass
        #for collection in self.all_collections:
        #    if utility.has_collection(collection) is False:
        #        constructor = getattr(
        #                CrystalMemoryConfig, 'Collection_'+collection
        #            )
        #        constructor(CrystalMemoryConfig.CrystalMemory['alias'])
