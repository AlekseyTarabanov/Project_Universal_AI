def deduplicate_by_prefix(chunks, prefix_len=50):
    seen = set()
    clean = []

    for chunk in chunks:
        prefix = chunk[:prefix_len]
        if prefix not in seen:
            seen.add(prefix)
            clean.append(chunk)

    return clean

