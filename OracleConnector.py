import cx_Oracle

connection = cx_Oracle.connect('wms_db' + '/' + 'Wms#2019' + '@45.76.177.65:1521/orcl')

sql = """
        select id as id, code as code from cat_user
    """

print("Get all rows via iterator")
cursor = connection.cursor()
for result in cursor.execute(sql):
    print(result[1])

cursor.close()
connection.close()