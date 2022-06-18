def base_query_builder(base_sql, search_parameters, search_conditions):
    conditions = []
    params = {}

    for key, value in search_parameters.items():
        if key in search_conditions:
            conditions.append(search_conditions[key])
            params[key] = '%' + search_parameters[key] + '%'

    where_statement = ' AND '.join(conditions)
    base_sql += " WHERE " + where_statement
    return base_sql, params
