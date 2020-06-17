from pony.orm import *
from src.conf.config import mysql_conf

db = Database()

db.bind(provider=mysql_conf['provider'], host=mysql_conf['host'], user=mysql_conf['user'], passwd=mysql_conf['passwd'],
        db=mysql_conf['db'])
print('DB_factory')

# class BaseDB(db.Entity):
#
#     @staticmethod
#     def before_insert():
#         print('insert 之前的操作')
#         pass
#
#     @staticmethod
#     def after_insert():
#         print('insert 之后的操作')
#
#     @staticmethod
#     def before_update():
#         print('update之前的操作')
#
#     @staticmethod
#     def after_update():
#         print('update之后的操作')
#
#     @staticmethod
#     def before_delete():
#         print('delete之前的操作')
#
#     @staticmethod
#     def after_delete():
#         print('delete之后的操作')
