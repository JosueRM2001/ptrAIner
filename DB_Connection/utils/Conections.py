import pymysql

mysql_connection = pymysql.connect(
    host='localhost',
    user='root',
    passwd='Mmnsin210606?',
    db='ptrainer_users')
cur = mysql_connection.cursor()

try:
    is_alive = mysql_connection.ping(reconnect=True)
    if is_alive:
        print("Pinged your deployment. You successfully connected toMySQL db!")
except Exception as e:
    print(e)