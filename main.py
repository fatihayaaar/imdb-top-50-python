import movie as mv
import mcapp as root
from tkinter import *
import threading
import os
from io import BytesIO
import urllib  
from PIL import Image, ImageTk
import webbrowser
import base64
from functools import partial
import requests
import ctypes 

#root eleman ve film nesnelerinin oluşturulması
rootApp = root.McAPP()
movies = rootApp.get_movies()
movie = movies[rootApp.state]

maintk = Tk()
maintk.geometry("1000x600+400+100")
maintk.title("Movie Center")
maintk.tk_setPalette("#2D2F30")
maintk.iconbitmap('icon.ico')
maintk.resizable(FALSE, FALSE)

buton_res1 = PhotoImage(file="back.png")
buton_res2 = ImageTk.PhotoImage(file="next.png")

#internetten film resimleri çekiyoruz
for i in range(0, len(movies)):
    urllib.request.urlretrieve(movies[i].get_banner(), "film_{}.png".format(movies[i].get_name()))

#filmlerin
#resimlerini pythonun anlayabileceği şekilde hafızaya alıyoruz
filmres = list()
for i in range(0, len(movies)):
    filmres.append(ImageTk.PhotoImage(Image.open("film_{}.png".format(movies[i].get_name())).resize((310, 450))))

resim_ekleme = Label(image=filmres[0])
resim_ekleme.place(x=10,y=10, w = 310, h = 450)

filmAdi = Label(text="Film adı: {}".format(movie.get_name()), font = "Times 24 bold")
filmAdi.place(x=350,y=4)

filmIMDB = Label(text="IMDB puanı: {}".format(movie.get_imbdpuan()),font = "Times")
filmIMDB.place(x=350,y=50)

filmYon = Label(text="Yönetmen: {}".format(movie.get_director()),font = "Times")
filmYon.place(x=350,y=90)

filmSen = Label(text="Senarist: {}".format(movie.get_scriptwriter()),font = "Times")
filmSen.place(x=350,y=130)

konuText = list()
def getKonu(m):
    konuText.clear()
    sayac = 0
    for i in range(0, len(m)):
        konuText.append(m[i])
        if sayac >= 65 and m[i] == " ":
            konuText.append("\n")
            sayac = 0
            continue
        sayac = sayac + 1

getKonu(movie.get_subject())

filmKonu = Label(text="Konu: {}".format(root.McAPP.listToString(konuText)), font = "Times", justify=LEFT)
filmKonu.place(x=350,y=210)

filmOyun = Label(text="Oyuncular: {}".format(movie.get_players()),font = "Times")
filmOyun.place(x=350,y=170)

#filmin fragman  url yönlendirilmesini yapıyoruz
def ilkfragman(url):
    webbrowser.open(url)

sayfaNo = Label(text="1", font = "Times 24", fg = "RoyalBlue1") 
sayfaNo.place(x=435,y=520)

sayNo = Label(text="/ 50", font = "Times 24", fg = "RoyalBlue1")   
sayNo.place(x=480,y=520)

link_git = Button(text="Fragmana git!",borderwidth=3,command=ilkfragman,padx=10,pady=10,font = "Times 16")
link_git.place(x=170,y=485)

#bu metotlarla birlikde film bilgilerini güncelliyoruz bu metot bir sonraki filmin değerlerini bu bileşenlere atıyor
def next_movie():
    if not(rootApp.state >= 49):
        #state ile sayfa numarasını kontrol ediyoruz
        rootApp.state = rootApp.state + 1
        movie = movies[rootApp.state]
        #config ile bileşenlerin özellikleri değiştiriliyor
        filmAdi.config(text="Film adı: {}".format(movie.get_name()))
        filmIMDB.config(text="IMDB puanı: {}".format(movie.get_imbdpuan()))
        filmYon.config(text="Yönetmen: {}".format(movie.get_director()))
        filmSen.config(text="Senarist: {}".format(movie.get_scriptwriter()))
        getKonu(movie.get_subject())
        filmKonu.config(text="Konu: {}".format(root.McAPP.listToString(konuText)))
        filmOyun.config(text="Oyuncular: {}".format(movie.get_players()))
        link_git.configure(command = partial(ilkfragman, movie.get_fragment()))
        resim_ekleme.config(image=filmres[rootApp.state])
        resim_ekleme.place(x=10,y=10)
        sayfaNo.config(text="{}".format(rootApp.state + 1))

#bu metot bir önceki filmin değerlerini bu bileşenlere atıyor
def back_movie():
    if not(rootApp.state <= 0):
        rootApp.state = rootApp.state - 1
        movie = movies[rootApp.state]
        #config ile bileşenlerin özellikleri değiştiriliyor
        filmAdi.config(text="Film adı: {}".format(movie.get_name()))
        filmIMDB.config(text="IMDB puanı: {}".format(movie.get_imbdpuan()))
        filmYon.config(text="Yönetmen: {}".format(movie.get_director()))
        filmSen.config(text="Senarist: {}".format(movie.get_scriptwriter()))
        getKonu(movie.get_subject())
        filmKonu.config(text="Konu: {}".format(root.McAPP.listToString(konuText)))
        filmOyun.config(text="Oyuncular: {}".format(movie.get_players()))
        link_git.configure(command = partial(ilkfragman, movie.get_fragment()))
        resim_ekleme.config(image=filmres[rootApp.state])
        resim_ekleme.place(x=10,y=10)
        sayfaNo.config(text="{}".format(rootApp.state + 1))

geri = Button(image=buton_res1,borderwidth=0, command = back_movie)
geri.place(x=45,y=510)

ileri = Button(image=buton_res2, borderwidth=0, command = next_movie)
ileri.place(x=890,y=510)

maintk.mainloop()
