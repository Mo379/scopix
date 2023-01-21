from pymilvus import (
        Collection,
        CollectionSchema,
        FieldSchema,
        DataType
    )


# Crystal memory connection config
CrystalMemory = dict(
        alias='default',
        host='0.0.0.0',
        port=19530,
    )


# Status collections
def Collection_Test():
    pk = FieldSchema(
            name='pk',
            dtype=DataType.INT64,
            is_primary=True
        )
    test_vec = FieldSchema(
            name='test_vec',
            dtype=DataType.FLOAT_VECTOR,
            dim=2
        )
    schema = CollectionSchema(
            fields=[pk, test_vec],
            description="Athena test collection"
        )
    collection_name = 'Athenas_test'
    Athena_status_collection = Collection(
            name=collection_name,
            schema=schema,
            using=CrystalMemory['alias'],
        )
    return Athena_status_collection
