def format_query_result(columns, query_object):
    names = list(map(lambda x: x[0], columns))

    results = {}
    for index, name in enumerate(names):
        results[name] = query_object[index]

    return results
