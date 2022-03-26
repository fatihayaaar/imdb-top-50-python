import movie as mv
import random as rnd
import os
import sqlite3 as sql

#root sınıfımız
class McAPP:
    __movie = None
    __movies = list()
    state = 0

    #kurucu metot
    def __init__(self):
        self.__movie = mv.Movie()
        self.get_data()
        
    @staticmethod
    def listToString(s):  
        str1 = ""  
        for ele in s:  
            str1 += ele     
        return str1  

    #veritabanından veri çekmek için yaptığımız metot
    def get_data(self):
        #sqlite veritabanı bağlantısı
        db = sql.connect("moviecenter.db")
        c = db.cursor()
        #sql select sorgusu
        c.execute('SELECT name, imbd, director, subject, scriptwriter, players, banner, fragment FROM movie')
        rows = c.fetchall()

        #sordugan çıkan satırlardaki kolonları movie nesnemize yüklediğmiz döngü
        for row in rows:
            self.__movie = mv.Movie()
            self.__movie.set_name(row[0])
            self.__movie.set_imbdpuan(row[1])
            self.__movie.set_director(row[2])
            self.__movie.set_subject(row[3])
            self.__movie.set_scriptwriter(row[4])
            self.__movie.set_players(row[5])
            self.__movie.set_banner(row[6])
            self.__movie.set_fragment(row[7])

            #filmler listesine film nesnesini ekliyoruz
            self.__movies.append(self.__movie)

    #private elemanlar için get ve set metotları
    def get_movie(self):
        return self.__movie

    def set_movie(self, movie):
        self.__movie = movie

    def get_movies(self):
        return self.__movies