def get_document(document_id, reader, cache):
    return cache.get_or_set(
        f"document:{document_id}",
        lambda: reader.get_document(document_id),
        ttl_seconds=3600,
    )


def update_document(document_id, fields, writer):
    return writer.update_document(document_id, fields)
