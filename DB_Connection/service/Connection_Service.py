from src.DB_Connection.utils.Conections import cur, mysql_connection


class Connection_Service:
    def get_id(username):
        cur.execute("SELECT id_usuario FROM usuario WHERE user_name = %s", (username,))
        for user in cur.fetchall():
            return user
        return None

    def get_height(username):
        cur.execute("SELECT height FROM usuario WHERE user_name = %s", (username,))
        for user in cur.fetchall():
            print(user[0])
            return user[0]
        return None

    def get_weight(username):
        cur.execute("SELECT weight FROM usuario WHERE user_name = %s", (username,))
        for user in cur.fetchall():
            print(user[0])
            return user[0]
        return None

    def get_age(username):
        cur.execute("SELECT age FROM usuario WHERE user_name = %s", (username,))
        for user in cur.fetchall():
            print(user[0])
            return user[0]
        return None

    def get_activity_factor(username):
        cur.execute("SELECT activity_factor FROM usuario WHERE user_name = %s", (username,))
        for user in cur.fetchall():
            print(user[0])
            return user[0]
        return None

    def get_genre(username):
        cur.execute("SELECT genre FROM usuario WHERE user_name = %s", (username,))
        for user in cur.fetchall():
            print(user[0])
            return user[0]
        return None

    def get_objective(username):
        cur.execute("SELECT objective FROM usuario WHERE user_name = %s", (username,))
        for user in cur.fetchall():
            print(user[0])
            return user[0]
        return None

    def get_neck(username):
        cur.execute("SELECT neck FROM usuario WHERE user_name = %s", (username,))
        for user in cur.fetchall():
            print(user[0])
            return user[0]
        return None

    def get_waist(username):
        cur.execute("SELECT waist FROM usuario WHERE user_name = %s", (username,))
        for user in cur.fetchall():
            print(user[0])
            return user[0]
        return None

    def get_hip(username):
        cur.execute("SELECT hip FROM usuario WHERE user_name = %s", (username,))
        for user in cur.fetchall():
            print(user[0])
            return user[0]
        return None

    def get_maintenance_calories(username):
        cur.execute("SELECT maintenance_calories FROM usuario WHERE user_name = %s", (username,))
        for user in cur.fetchall():
            print(user[0])
            return user[0]
        return None

    def get_objective_calories(username):
        cur.execute("SELECT objective_calories FROM usuario WHERE user_name = %s", (username,))
        for user in cur.fetchall():
            print(user[0])
            return user[0]
        return None

    def get_body_fat(username):
        cur.execute("SELECT fat_percent FROM usuario WHERE user_name = %s", (username,))
        for user in cur.fetchall():
            print(user[0])
            return user[0]
        return None

    def get_hidratation(username):
        cur.execute("SELECT hidratation FROM usuario WHERE user_name = %s", (username,))
        for user in cur.fetchall():
            print(user[0])
            return user[0]
        return None

    def get_protein(username):
        cur.execute("SELECT protein FROM usuario WHERE user_name = %s", (username,))
        for user in cur.fetchall():
            print(user[0])
            return user[0]
        return None

    def get_carbs(username):
        cur.execute("SELECT carbs FROM usuario WHERE user_name = %s", (username,))
        for user in cur.fetchall():
            print(user[0])
            return user[0]
        return None

    def get_fat(username):
        cur.execute("SELECT fat FROM usuario WHERE user_name = %s", (username,))
        for user in cur.fetchall():
            print(user[0])
            return user[0]
        return None

    def confirm_user(username):
        cur.execute("SELECT id_usuario FROM usuario WHERE user_name = %s", (username,))
        for user in cur.fetchall():
            try:
                if user[0] is not None:
                    return True
                elif user is not None:
                    return False
                else:
                    return False
            except Exception as e:
                print(e)

    def get_user(username):
        cur.execute("SELECT * FROM usuario WHERE user_name = %s", (username,))
        for user in cur.fetchall():
            return user
        return None

    def fill_survey(username: str, height: float, weight: float, age: int, genre: str, activity_factor: str,
                    objective: str, neck: float, waist: float, hip: float):
        cur.execute("UPDATE usuario SET height = %s WHERE user_name = %s", (height, username))
        cur.execute("UPDATE usuario SET weight = %s WHERE user_name = %s", (weight, username))
        cur.execute("UPDATE usuario SET age = %s WHERE user_name = %s", (age, username))
        cur.execute("UPDATE usuario SET genre = %s WHERE user_name = %s", (genre, username))
        cur.execute("UPDATE usuario SET activity_factor = %s WHERE user_name = %s", (activity_factor, username))
        cur.execute("UPDATE usuario SET objective = %s WHERE user_name = %s", (objective, username))
        cur.execute("UPDATE usuario SET neck = %s WHERE user_name = %s", (neck, username))
        cur.execute("UPDATE usuario SET waist = %s WHERE user_name = %s", (waist, username))
        cur.execute("UPDATE usuario SET hip = %s WHERE user_name = %s", (hip, username))
        mysql_connection.commit()

    def update_height(username, height):
        cur.execute("UPDATE usuario SET height = %s WHERE user_name = %s", (height, username))
        mysql_connection.commit()

    def update_weight(username, weight):
        cur.execute("UPDATE usuario SET weight = %s WHERE user_name = %s", (weight, username))
        mysql_connection.commit()

    def update_age(username, age):
        cur.execute("UPDATE usuario SET age = %s WHERE user_name = %s", (age, username))
        mysql_connection.commit()

    def update_genre(username, genre):
        cur.execute("UPDATE usuario SET genre = %s WHERE user_name = %s", (genre, username))
        mysql_connection.commit()

    def update_activity_factor(username, activity_factor):
        cur.execute("UPDATE usuario SET activity_factor = %s WHERE user_name = %s", (activity_factor, username))
        mysql_connection.commit()

    def update_objective(username, objective):
        cur.execute("UPDATE usuario SET objective = %s WHERE user_name = %s", (objective, username))
        mysql_connection.commit()

    def update_maintenance_calories(username, maintenance_calories):
        cur.execute("UPDATE usuario SET maintenance_calories = %s WHERE user_name = %s",
                    (maintenance_calories, username))
        mysql_connection.commit()

    def update_objective_calories(username, objective_calories):
        cur.execute("UPDATE usuario SET objective_calories = %s WHERE user_name = %s", (objective_calories, username))
        mysql_connection.commit()

    def update_protein(username, protein):
        cur.execute("UPDATE usuario SET protein = %s WHERE user_name = %s", (protein, username))
        mysql_connection.commit()

    def update_carbs(username, carbs):
        cur.execute("UPDATE usuario SET carbs = %s WHERE user_name = %s", (carbs, username))
        mysql_connection.commit()

    def update_fat(username, fat):
        cur.execute("UPDATE usuario SET fat = %s WHERE user_name = %s", (fat, username))
        mysql_connection.commit()

    def update_hidratation(username, hidratation):
        cur.execute("UPDATE usuario SET hidratation = %s WHERE user_name = %s", (hidratation, username))
        mysql_connection.commit()

    def update_neck(username, neck):
        cur.execute("UPDATE usuario SET neck = %s WHERE user_name = %s", (neck, username))
        mysql_connection.commit()

    def update_waist(username, waist):
        cur.execute("UPDATE usuario SET waist = %s WHERE user_name = %s", (waist, username))
        mysql_connection.commit()

    def update_hip(username, hip):
        cur.execute("UPDATE usuario SET hip = %s WHERE user_name = %s", (hip, username))
        mysql_connection.commit()

    def update_fat_percent(username, fat_percent):
        cur.execute("UPDATE usuario SET fat_percent = %s WHERE user_name = %s", (fat_percent, username))
        mysql_connection.commit()

    def update_activity(username, activity):
        cur.execute("UPDATE usuario SET activity = %s WHERE user_name = %s", (activity, username))
        mysql_connection.commit()
