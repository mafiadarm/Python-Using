#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           03_20_2018  9:22
    File Name:      /GitHub/sql_query
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:

==============================
"""

import pymssql

__author__ = 'Loffew'


class SqlConnect:
    def __init__(self, database):
        try:
            self.conn = pymssql.connect(**database, charset="GBK")
            self.curr = self.conn.cursor()
        except Exception as e:
            raise e

    def close(self):
        self.curr.close()
        self.conn.close()

    def query_data(self, sql_sentence):
        try:
            self.curr.execute(sql_sentence)
            result = self.curr.fetchall()
        except Exception as e:
            raise e
        finally:
            self.close()
        return result


if __name__ == '__main__':
    pass
