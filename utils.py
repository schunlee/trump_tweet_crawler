#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os

__author__ = "bill.li"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, "database")


def read_sql(sql_name):
    sql_path = os.path.join(BASE_DIR, "sql", sql_name)
    with open(sql_path) as f:
        content = f.read()
    return content


if __name__ == '__main__':
    pass
