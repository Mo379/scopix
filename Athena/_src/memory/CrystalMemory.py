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
        self.all_collections = [
                'Test',
            ]
        self._create_collections()
        self._migrate()

    def _insert(self, collection, data):
        """ Insert data of matching schema into the collection """
        pass

    def _create_collections(self):
        """ A helper function that creates all collections used by athena

        loops through the hardcoded list of collection names, checks if they
        exist in the vector DB and creates them using a function defined
        in the CrystalMemoryConfig file.
        """
        for collection in self.all_collections:
            if utility.has_collection(collection) is False:
                constructor = getattr(
                        CrystalMemoryConfig, 'Collection_'+collection
                    )
                constructor()
    def _migrate(self):
        """ A helper function that migrates the database from a save version
        """
        pass
