#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import youtube_dl
from tkinter import *
from tkinter import ttk
import json
import os

class Aplicacion():
	def __init__(self):
		self.raiz=Tk()
		self.raiz.geometry('400x300')
		self.raiz.configure(bg='gray25')
		self.raiz.title('Aplicación')

		etiqueta=Label(self.raiz,text='Pon aqui tu enlace',bg='gray25',fg='white')
		etiqueta.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)

		self.urele = StringVar()

		etiqueta.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)

		ctext = ttk.Entry(self.raiz, textvariable=self.urele)
		ctext.pack(side=TOP, fill=BOTH, padx=5, pady=5)

		separ1 = ttk.Separator(self.raiz, orient=HORIZONTAL)
		separ1.pack(side=TOP, fill=BOTH, padx=5, pady=5)

		desboton=ttk.Button(self.raiz, text='Descargar', command=self.descarga).pack(side=LEFT, fill=BOTH, padx=5, pady=5)
		
		muboton=ttk.Button(self.raiz, text='m3u', command=self.lista).pack(side=LEFT, fill=BOTH, padx=5, pady=5)

		salboton=ttk.Button(self.raiz, text='Salir', command=self.raiz.destroy).pack(side=RIGHT, fill=BOTH, padx=5, pady=5)

		self.raiz.mainloop()

	def descarga(self):
		options = {
		'format' :'bestaudio/best',
		'extractaudio' : True,
		'audioformat' : 'mp3',
		'outtmpl':'%(title)s',
		'noplaylist' : True,
		} 
		with youtube_dl.YoutubeDL(options) as ydl:
			ydl.download([self.urele.get()])
		
	def lista(self):
		
		options = {
		'format' :'bestaudio/best',
		'simulate' : True,
		#'noplaylist' : True,
		}
		with youtube_dl.YoutubeDL(options) as ydl:
			result = ydl.extract_info(self.urele.get())
		if 'entries' in result:
			video = []
		    # Can be a playlist or a list of videos
			son = len(result['entries'])
			for i in range(son):
				entrada=result['entries'][i]
				video.append(entrada)
		else:
		    # Just a video
			video = result
		#print(video)
		escribelo(video)
		#video_url = video['url']
		#titulo_url = video['title']
		#print(video_url)
		#print(titulo_url)

	
def escribelo(v):

	encabezado = '#EXTM3U\n'
	lineas= '\n'
	#tit=t
	if 'title' in v:
		lista = open('single.m3u','w')
		tit=v['title']
		line=v['url']
		lineas+='\n#EXTINF:0,{}\n'.format(tit)+line+'\n'
		
	else:
		lista = open('lista.m3u','w')
		for i in range(0,len(v)):

			#line=l[i][2:54]
			tit=v[i]['title']
			line=v[i]['url']
			lineas+='\n#EXTINF:0,{}\n'.format(tit)+line+'\n'		
		

		
	#lista = open('lista.m3u','w')
	lista.write(encabezado+lineas)
	lista.close()
	
def main():
	mi_app=Aplicacion()

if __name__=='__main__':

	main()
	