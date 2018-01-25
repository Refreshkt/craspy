# -*- coding: utf-8 -*-

import json

def leelo(j):
	leer = json.loads(j)
	title = str(leer[0]['link'])

	

	for i in range(0,len(leer)):

		if leer[i]['link']:
			linkstr=str(leer[i]['link'])
			links.append(linkstr)

def titulalo(l):
	for i in range(0,len(l)):

		tit=l[i].split('/')
		if tit[6].find('_')==-1:
			tit1=tit[6].split('-')
		else:
			tit1=tit[6].split('_')
		
		tit2 = ' '.join(tit1)
		tit3 = tit2.split(',')
		titulo = ' '.join(tit3)
		titulos.append(titulo)

def escribelo(t,l):

	encabezado = '#EXTM3U\n'
	lineas= '\n'
	tit=t
	for i in range(0,len(l)):

		lineas+='\n#EXTINF:0,{}\n'.format(tit[i])+l[i]+'\n'

	lista = open('mtorrent.m3u','w')
	lista.write(encabezado+lineas)
	lista.close()

if __name__=='__main__':

	titulos=[]

	links=[]
	
	jeison=open('mtorrent.json').read()
	
	leelo(jeison)
	
	titulalo(links)

	escribelo(titulos,links)