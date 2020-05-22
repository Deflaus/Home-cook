# -*- coding: utf-8 -*-
import sqlite3
my_file = "recips.db"


class DataBaseAccess(object):
    @staticmethod
    def parse_titles():
        dict_titles = dict()
        try:
            con = sqlite3.connect(my_file)
            cur = con.cursor()

            cur.execute("SELECT * FROM titles")

            data = cur.fetchall()

            cur.close()
            con.close()

            for i in data:
                dict_titles[i[0]] = i[1]
            return dict_titles
        except:
            print(-1)

    @staticmethod
    def parse_rate():
        dict_rate = dict()
        try:
            con = sqlite3.connect(my_file)
            cur = con.cursor()

            cur.execute("SELECT * FROM rate")

            data = cur.fetchall()

            cur.close()
            con.close()

            for i in data:
                dict_rate[i[0]] = i[1]
            return dict_rate
        except:
            print(-1)

    @staticmethod
    def parse_conform():
        dict_conform = dict()
        try:
            con = sqlite3.connect(my_file)
            cur = con.cursor()

            cur.execute("SELECT * FROM recipes")

            data = cur.fetchall()

            cur.close()
            con.close()

            for i in data:
                dict_conform[i[0]] = i[1]
            return dict_conform
        except:
            print(-1)

    @staticmethod
    def parse_recipes():
        dict_recipes = dict()
        try:
            con = sqlite3.connect(my_file)
            cur = con.cursor()

            cur.execute("SELECT * FROM recipes")

            data = cur.fetchall()

            cur.close()
            con.close()

            for i in data:
                dict_recipes[i[0]] = i[2]
            return dict_recipes
        except:
            print(-1)

    @staticmethod
    def parse_ingridients():
        dict_ingridients = dict()
        try:
            con = sqlite3.connect(my_file)
            cur = con.cursor()

            cur.execute("SELECT * FROM ingridients")

            data = cur.fetchall()

            cur.close()
            con.close()

            for i in data:
                dict_ingridients[i[1]] = i[0]
            return dict_ingridients
        except:
            print(-1)

    @staticmethod
    def update_rate(id, rate):
        try:
            con = sqlite3.connect(my_file)
            cur = con.cursor()

            cur.execute('UPDATE rate SET Rate = ' + str(rate) + ' WHERE IDofIngr = ' + str(id) + ' ')
            con.commit()

            cur.close()
            con.close()
        except:
            print(-1)




