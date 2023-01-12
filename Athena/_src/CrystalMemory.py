from _src.config import CrystalMemoryConfig
from pymilvus import (
        connections,
        utility
    )


class _CrystalMemory():
    """ A vector database API, that fetches Athena's crystal memory

    This class enables athena to directetly fetch information from her
    vector database using estimated neural network embedding vectors.
    """
    def __init__(self):
        # Create a connection to Vector DB
        connections.connect(
          alias=CrystalMemoryConfig.CrystalMemory['alias'],
          host=CrystalMemoryConfig.CrystalMemory['host'],
          port=CrystalMemoryConfig.CrystalMemory['port']
        )
        all_collections = [
                'Athena_status',
            ]
        for collection in all_collections:
            print(collection)
            print(utility.has_collection(collection))

        self._migrate()

    def _disconnect(self):
        connections.disconnect(CrystalMemoryConfig.CrystalMemory['alias'])

    def _migrate(self):
        pass
