#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sqlite3

from utils import read_sql, DB_DIR

__author__ = "bill.li"

DB_NAME = os.path.join(DB_DIR, "tweet_info.db")


def init_table(num=3):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        i = 0
        while i < num:
            try:
                cursor.execute(read_sql("create_tweet_table.sql"))
                break
            except sqlite3.OperationalError:
                cursor.execute(read_sql("delete_tweet_table.sql"))
                continue


def insert(id, title, trans_title, time_str):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        data = [id, title, trans_title, time_str]
        cursor.executemany(read_sql("insert_tweet_table.sql"), [data])
        conn.commit()


def search(id):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        targets = cursor.execute(read_sql("search_tweet_table.sql").format(id)).fetchall()
        return len(targets)


def search_all():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        targets = cursor.execute(read_sql("search_all_tweet_table.sql")).fetchall()
        return len(targets)


if __name__ == '__main__':
    pass
    search_all()
