def search(collection, value):
    """
    collection에서 value를 여러 번 검색합니다.
    """
    for i in range(50000):
        found = value in collection
        