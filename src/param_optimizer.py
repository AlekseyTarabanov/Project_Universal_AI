def optimize_params(text: str, query: str):
    text_len = len(text)
    query_len = len(query.split())

    # CHUNK_SIZE
    if text_len < 5_000:
        chunk_size = 100
    elif text_len < 20_000:
        chunk_size = 130
    else:
        chunk_size = 180

    # TOP_K
    top_k = 5
    if query_len <= 3:
        top_k += 2
    if text_len > 20_000:
        top_k += 1

    return chunk_size, top_k

