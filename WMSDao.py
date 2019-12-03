#!/opt/rh/rh-python36/root/usr/bin/python3
import cx_Oracle


def getConnection():
    return cx_Oracle.connect('wms_db' + '/' + 'Wms#2019' + '@45.76.177.65:1521/orcl')


def close(cursor, connection):
    cursor.close()
    connection.close()


def getTotalTransByType(type):
    connection = getConnection()
    result = 0
    sql = """
            select count(*) total_trans from mjr_stock_trans trans
            where trans.created_date >= TRUNC(SYSDATE)
            and trans.CREATED_DATE < trunc(sysdate+1)
            and type = 
            """ + str(type)
    cursor = connection.cursor()
    for result in cursor.execute(sql):
        result = result[0]

    close(cursor, connection)
    return result


def getTotalTransByCusMessage():
    connection = getConnection()
    mainMessage = 'Total transaction by customer:\n'

    sql = """
            select cus.name cust_name, count(*) total_trans from mjr_stock_trans trans
        left join CAT_CUSTOMER cus on cus.id = trans.cust_id
        where trans.created_date >= TRUNC(SYSDATE)
        and trans.CREATED_DATE < trunc(sysdate + 1)
        group by cust_id, cus.name
        """

    cursor = connection.cursor()
    for result in cursor.execute(sql):
        mainMessage += str(result[0]) + ': ' + str(result[1]) + '\n'

    close(cursor, connection)

    return mainMessage
