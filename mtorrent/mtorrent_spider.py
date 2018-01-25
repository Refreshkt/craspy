# -*- coding: utf-8 -*-
import scrapy

########################################################################################################################
### Spider para la creación de un json con los enlaces de descarga de los archivos torrent de la pagina mejortorrent ###
########################################################################################################################
########################################################################################################################
###                                                                                                                  ###
###                                scrapy runspider mtorrent_spider.py -o mtorrent.json                              ###
###                                                                                                                  ###
########################################################################################################################
# declaramos la clase MtorrentSpider que es como el nombre del archivo pero en CamelCase
# esta clase extiende de scrapy.Spider

class MtorrentSpider(scrapy.Spider):

	# en un proyecto scrapy se pueden crear varios spiders que deberemos nombrar de forma diferente
	name = "torrents"

	# la funcion start_request es la que inicia las llamadas, aqui podría ir una lista de urls a seguir
	def start_requests(self):

		# en este caso hacemos solo una llamada a una url y llamamos a una nueva fucion que manejara el resultado
		yield scrapy.Request('http://www.mejortorrent.com/torrents-de-peliculas-hd-alta-definicion.html', self.parse_page2)
		###                                               callback=self.parse_page2                                          ###

	# esta funcion recibe el resultado de start_request en la variable response
	# la variable response contiene ahora el html de la pagina solicitada en start_request
	def parse_page2(self,response):

		# guardamos la url básica del sitio por que su estructura de enlaces internos es relativa
		iniroute = 'http://www.mejortorrent.com'

		# iteramos por el dom de la respuesta y extraemos cada enlace con xpath
		for linke in response.xpath('/html/body/table/tr[3]/td/table/tr/td[2]/table/tr/td/table/tr[3]/td/table/tr/td/div/a/@href').extract():

			# cada enlace extraido se completa con la url basica de la variable iniroute en la llamada scrapy.Request()
			# y se envia la llamada a la url completa a una siguiente funcion que manejará el resultado
			yield scrapy.Request(iniroute+linke, callback=self.parse_page3)

	# esta función recibe los resultados de la anterior conforme se van generando en el for
	# los resultados tambien son el html como en la función anterior
	def parse_page3(self,response):

		# el tema de los enlaces relativos
		iniroute = 'http://www.mejortorrent.com/'

		# otra iteración por el dom con su extracción de enlaces con xpath
		for downlink in response.xpath('/html/body/table/tr[3]/td/table/tr/td[2]/table/tr/td/table[1]/tr/td[2]/table/tr/td/a/@href').extract():

			# y enviamos los enlaces completos que se van generando a la función parse
			yield scrapy.Request(iniroute+downlink, callback=self.parse)

	# la funcion parse es la que recibe el resultado del spider y lo envia a la salida del archivo mtorrent.json
	def parse(self, response):

		iniroute='http://www.mejortorrent.com'

		for lntor in response.xpath('//*[@id="contenido_descarga"]/table/tr/td/table/tr/td/table/tr/td/a/@href').extract():
			
			# cada par key value que genera el for se envia para la creación del .json 
			yield {
				'link':iniroute+lntor
			}

	