def rebuild_workspace(workspace_id, reader, search):
    documents = reader.list_documents(workspace_id)
    for document in documents:
        search.replace(document.id, {
            "title": document.title,
            "description": document.description,
        })
    search.remove_missing(workspace_id, [document.id for document in documents])
