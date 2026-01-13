import re

def keyword_boost(query, ranked, boost=0.15):
    keywords = re.findall(r"\w+", query.lower())

    boosted = []
    for chunk, score in ranked:
        bonus = 0.0
        text = chunk.lower()

        for kw in keywords:
            if len(kw) >= 4 and kw in text:
                bonus += boost

        boosted.append((chunk, score + bonus))

    return boosted

