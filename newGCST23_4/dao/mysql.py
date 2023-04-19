import pandas as pd

from dao import connection


con = connection.mysql()
def executeSQL(sql):
    con.cursor.execute(sql)
    con.DB.commit()


def insert(columns, values):
    sql = f'INSERT INTO table_name ({columns}) VALUES ({values});'
    print(sql)
    executeSQL(sql)


def delete(tableName, condition):
    sql = f'delete from {tableName} where {condition}'
    print(sql)
    executeSQL(sql)


def update(tableName, columns_values, condition):
    sql = f'UPDATE {tableName} SET {columns_values} where {condition}'
    print(sql)
    executeSQL(sql)


def select(tableName, columns='*', Wvalue=None, Lvalue=None, Ovalue=None, orderByColumn="`index`"):
    sql = f'SELECT {columns} FROM {tableName}'
    if Wvalue:
        sql += f' WHERE {Wvalue}'
    if Lvalue:
        sql += f' LIMIT {Lvalue}'
    if Ovalue:
        sql += f' OFFSET {Wvalue}'
    sql += f' order by {orderByColumn}'
    print(sql)
    return pd.read_sql(sql, con.DB_SQLAlchemy).fillna('').astype(str)
