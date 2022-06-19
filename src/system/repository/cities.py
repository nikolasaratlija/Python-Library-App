from src.system.context import Context


def get_cities():
    con = Context.db_connection
    c = con.cursor()
    c.execute("SELECT * FROM cities")
    return c.fetchall()
