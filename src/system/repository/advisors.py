from src.system.context import Context

from src.system.util.query_result_formatter import format_query_result


def get_advisor(member_id):
    con = Context.db_connection
    c = con.cursor()
    c.execute("SELECT * FROM users WHERE id = ? AND role_id = 3", (member_id,))

    advisor = c.fetchone()

    if not advisor:
        return None

    return format_query_result(c.description, advisor)
