from src.system.context import Context
from src.system.util.query_result_formatter import format_query_result


def get_member(member_id):
    con = Context.db_connection
    c = con.cursor()
    c.execute("SELECT * FROM members WHERE id = ? ", (member_id,))

    member = c.fetchone()

    if not member:
        return None

    return format_query_result(c.description, member)
