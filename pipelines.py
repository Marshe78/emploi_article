# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#from itemadapter import ItemAdapter
import mysql.connector


class Database:
    def connectDb():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
        )
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS emploi")

    def createTable():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="emploi"
        )
        mycursor = mydb.cursor()
        #mycursor.execute("CREATE TABLE IF NOT EXISTS movie (title VARCHAR(255), img VARCHAR(255), author VARCHAR(255), time VARCHAR(255), genre VARCHAR(255), score VARCHAR(255), description TEXT(50000), releaseDate VARCHAR(255))")
        mycursor.execute(
            "CREATE TABLE IF NOT EXISTS article (title VARCHAR(255), attachement_file VARCHAR(255), img VARCHAR(255), date VARCHAR(255))")

    def addRow(item):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="emploi"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO article (title, attachement_file, img, date) VALUES (%s, %s, %s, %s)"
        val = (item['title'], item['attachement_file'],
               item['img'], item['date'])
        mycursor.execute(sql, val)
        mydb.commit()
        # print("Title :" , type(item['title']) , "Img :" , type(item['img']) , "Author :" , type(item['author']) , "Time :" , type(item['time']) , "Genre :" , type(item['genre']) , "Score :" , type(item['score']) , "Description :" , type(item['desc']) , "Release Date :" , type(item['release']))

    def addRowEmploi(item):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="emploi"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO article (title, attachement_file, img, date) VALUES ( %s, %s, %s, %s, %s, %s)"
        val = (item['title'], item['attachement_file'],
               item['img'], item['date'])
        mycursor.execute(sql, val)
        mydb.commit()
