import mysql.connector
database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'munna@4516'
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE dcr")
print('ALL DONE')
