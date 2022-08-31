#Importação de bibliotecas que serão usadas para o funcionamento da assistente
import re
import speech_recognition as sr
import pyttsx3
from config import *
from random import choice
import datetime
import os

#Reprodutor de voz
reproducao = pyttsx3.init()

#Função que define a saida de audio 
def sai_som(reposta):
	reproducao.say(reposta)
	reproducao.runAndWait()

#Definição geral da CEOS
def CEOS():
	print("Oi, qual  é o seu nome?")
	sai_som("Oi, qual é o seu nome?")
	while True:
		resposta_erro_aleatoria = choice(lista_erros)
		rec = sr.Recognizer()

		with sr.Microphone() as s:
			rec.adjust_for_ambient_noise(s)

			while True:
				try:
					audio = rec.listen(s)
					user_name = rec.recognize_google(audio, language="pt")
					user_name = verifica_nome(user_name)
					name_list()
					apresentacao = "{}".format(verifica_nome_exist(user_name))
					print(apresentacao)
					sai_som(apresentacao)
		
					brute_user_name = user_name
					user_name = user_name.split(" ")
					user_name = user_name[0]
					break
				except sr.UnknownValueError:
					sai_som(resposta_erro_aleatoria)
			break


	print("="* len(apresentacao))
	print("Em que posso te ajudar hoje?")
	sai_som("Em que posso te ajudar hoje?")

	while True:
		resposta_erro_aleatoria = choice(lista_erros)
		rec = sr.Recognizer()

		with sr.Microphone() as s:
			rec.adjust_for_ambient_noise(s)

			while True:
				try:
					audio = rec.listen(s)
					entrada = rec.recognize_google(audio, language="pt")
					print("{}: {}".format(user_name, entrada))

					#Chamada para perguntar as horas
					if "Que horas são" in entrada:
						resposta = time()

					elif "Que dia é hoje" in entrada:
						resposta = date()

					elif "Abrir bloco de notas" in entrada:
						sai_som("Abrindo bloco de notas")
						print("Abrindo bloco de notas")
						resposta = os.system("notepad.exe")

					elif "Abrir calculadora" in entrada:
						sai_som("Abrindo a calculadora")
						print("Abrindo a calculadora")
						resposta = os.system("calc.exe")

					elif "Abrir cmd" in entrada:
						sai_som("Abrindo CMD")
						print("Abrindo CMD")
						resposta = os.system("cmd.exe")

					elif "Abrir painel de controle" in entrada:
						sai_som("Abrindo painel de controle")
						print("Abrindo painel de controle")
						resposta = os.system("control.exe")

					elif "Abrir paint" in entrada:
						sai_som("Abrindo o paint")
						print("Abrindo o paint")
						resposta = os.system("mspaint.exe")
					
					elif "abrir Opera" or "Abrir opera" or "abrir ópera" in entrada:
						sai_som("Abrindo Opera GX")
						print("Abrindo OperaGX")
						resposta = os.system('"C:/Users/Anthony/AppData/Local/Programs/Opera GX/opera.exe"')

					elif "Abrir Spotify" in entrada:
						sai_som("Abrindo spotify")
						print("Abrindo Spotify")
						resposta = os.system('"C:/Users/Anthony/AppData/Roaming/Spotify/Spotify.exe"')
					
					elif "Abrir discord" in entrada:
						sai_som("Abrindo o discord")
						print("Abrindo o discord")
						resposta = os.system('"C:/Users/Anthony/AppData/Local/Discord/Update.exe"')

					elif "Abrir liga das lendas" or "abrir Liga das lendas" in entrada:
						sai_som("Abrindo o league of legends")
						print("Abrindo o league of legends")
						resposta = os.system('"C:/Riot Games/League of Legends/LeagueClient.exe"')
					
					#Chamada para perguntar sobre a temperatura 
					elif "qual é a temperatura de hoje" in entrada:

						lista_tempo = temperatura()
						temp = lista_tempo[0]
						temp_max = lista_tempo[1]
						temp_min = lista_tempo[2]

						resposta = "A temperatura de hoje é {:.2f}º. Temos uma máxima de {:.2f}º e uma minima de {:.2f}º".format(temp, temp_max, temp_min)
					
					#Chamada para informações gerais sobre a cidade
					elif "informações" in entrada and "cidade" in entrada:

						resposta = "Mostrando informações da cidade"
					else:
						resposta = conversas[entrada]

					if resposta == "Mostrando informações da cidade":

						lista_infos = clima_tempo()
						longitude = lista_infos[0]
						latitude = lista_infos[1]
						temp = lista_infos[2]
						pressao_atm = lista_infos[3]
						humidade = lista_infos[4]
						temp_max = lista_infos[5]
						temp_min = lista_infos[6]
						v_speed = lista_infos[7]
						v_direc = lista_infos[8]
						nebulosidade = lista_infos[9]
						id_da_cidade = lista_infos[10]

						print("CEOS:")
						print("Mostrando informações de {}\n\n".format(cidade))
						sai_som("Mostrando informações de {}".format(cidade))
						print("Longitude: {}, Latitude: {}\nId: {}\n".format(longitude, latitude, id_da_cidade))
						print("Temperatura: {:.2f}º".format(temp))
						print("Temperatura máxima: {:.2f}º".format(temp_max))
						print("Temperatura mínima: {:.2f}º".format(temp_min))
						print("Humidade: {}".format(humidade))
						print("Nebulosidade: {}".format(nebulosidade))
						print("Velocidade do vento: {}m/s\nDireção do vento: {}".format(v_speed, v_direc))

						
					else:
						print("CEOS: {}".format(resposta))
						sai_som("{}".format(resposta))

				except sr.UnknownValueError:
					sai_som(resposta_erro_aleatoria)
				except KeyError:
					pass


if __name__ == '__main__':
	intro()
	sai_som("Iniciando")
	CEOS()
