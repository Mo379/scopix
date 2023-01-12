from pymilvus import (
        Collection,
        CollectionSchema,
        FieldSchema,
        DataType
    )


# Crystal memory connection config
CrystalMemory = dict(
        alias='CrystalMemory',
        host='localhost',
        port=19530,
    )


# Status collections
def Collection_Athena_status():
    pk = FieldSchema(
            name='pk',
            dtype=DataType.INT64,
            is_primary=True
        )
    athena_status = FieldSchema(
            name='athena_status',
            dtype=DataType.VARCHAR,
        )
    last_updated = FieldSchema(
            name='last_updated',
            dtype=DataType.FLOAT,
        )
    schema = CollectionSchema(
            fields=[pk, athena_status, last_updated],
            description="Athena's current status"
        )
    collection_name = 'Athenas_status'
    Athena_status_collection = Collection(
            name=collection_name,
            schema=schema,
            using='CrystalMemory',
        )
    return Athena_status_collection
