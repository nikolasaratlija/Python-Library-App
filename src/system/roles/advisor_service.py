from src.system.roles.member import Member
from src.system.context import Context
from src.system.security.user_id_generator import generate_user_id
from src.system.logging.logger import log
from sqlite3 import IntegrityError

from src.system.util.query_builder import base_query_builder


def update_own_password(new_password):
    con = Context.db_connection
    c = con.cursor()

    c.execute("UPDATE users SET password = ? WHERE id = ?", (new_password, Context.user_id))

    if c.rowcount == 1:
        con.commit()
        log("User updated password", f"User #{Context.user_id} update their own password")
        return True, "Your password has been successfully updated."
    else:
        return False, "Something went wrong while trying to update your password."


def add_member(member: Member):
    # TODO: add fields
    con = Context.db_connection
    c = con.cursor()

    user_id = generate_user_id()

    try:
        c.execute("INSERT INTO members (id, first_name, last_name) VALUES (?, ?)",
                  (user_id, member.first_name, member.last_name))
        con.commit()
        log("Member Added", f"Member '#{user_id} has been added to the system'")
        return True, "Member Added", f"Member '#{user_id} has been added to the system'"
    except IntegrityError:
        return False, "user_id already exists."


def modify_member():
    pass


def read_member(search_parameters):
    con = Context.db_connection
    c = con.cursor()
    sql, params = _read_member_query_builder(search_parameters)

    c.execute(sql, params)
    result = c.fetchone()

    if not result:
        return False, "User cannot be found"

    return True, result


def _read_member_query_builder(search_parameters):
    # TODO TRY CATCH
    search_conditions = {
        'id': 'm.id LIKE :id',
        'first_name': 'first_name LIKE :first_name',
        'last_name': 'last_name LIKE :last_name',
        'email': 'email LIKE :email',
        'phone': 'phone LIKE :phone',
        'street_name': 'street_name LIKE :street_name',
        'house_number': 'house_number LIKE :house_number',
        'zip_code': 'zip_code LIKE :zip_code',
        'city_name': 'c.city_name LIKE :city_name',
    }

    sql = "SELECT m.id, first_name, last_name, email, phone, street_name, house_number, zip_code, c.city_name " \
          "FROM members m JOIN cities c on m.city_id = c.id"

    return base_query_builder(sql, search_parameters, search_conditions)
