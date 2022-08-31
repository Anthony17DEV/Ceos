#Importações usadas durante o aplicativo
from logging import exception
import requests as rq
import datetime

#Anotação de versões
version = "1.13.0"
cidade = 'Tibau'

#Introdução do aplicativo
def intro():
	msg = "CEOS - Versão {} / by: AnthonyYNF".format(version)
	print("-" * len(msg) +  "\n{}\n".format(msg)  +   "-" * len(msg))

#Lista de erros usadas para a resposta da assistente
lista_erros = [
		"Não consegui entender, repita por favor",
		"Desculpe, não entendi",
		"Repita novamente por favor"
]

#Convesasão usada para inicio do projeto
conversas = {
	"Olá": "oi, tudo bem?",
	"Olá Olá": "oi, tudo bem?",
	"Oi": "oi, tudo bem?",
	"E aí": "E aí, tudo bem?",
	"Sim e com você": "Estou bem obrigada por perguntar",
	"Tudo sim e com você": "Estou bem obrigada por perguntar",
	"Tudo sim e contigo": "Estou bem obrigada por perguntar",
	"Estou legal e você": "Estou bem obrigada por perguntar",
	"Tudo": "Que ótimo",
	"Tudo sim": "Maravilha",
	"Tudo otimo": "Que bom",
	"Tudo perfeito": "Que bom",
	"Tudo maravilhoso": "Que bom",
	"Tudo ok": "Que bom",
	"Estou legal": "Que bom",
	"Não": "Que pena",
	"Não estou legal": "Que triste",
	"Estou pessimo": "Que pena",
	"Estou mal": "Que triste",
	"Estou cabis baixo": "Que pena",
	"Estou triste": "Que pena",
	"E com você": "Estou bem obrigada por perguntar",
	"E contigo": "Estou bem obrigada por perguntar",
	"E você": "Estou bem obrigada por perguntar",
	"E você como vai?": "Estou bem obrigada por perguntar",
	"sim e você": "Estou bem obrigada por perguntar",
}

comandos = {
	"desligar": "desligando",
	"reiniciar": "reiniciando"
}

#Definição para verificação do nome do usuario e reconhecimento
def verifica_nome(user_name):
	if user_name.startswith("Meu nome é"):
		user_name = user_name.replace("Meu nome é", "")
	if user_name.startswith("Eu me chamo"):
		user_name = user_name.replace("Eu me chamo", "")
	if user_name.startswith("Eu sou o"):
		user_name = user_name.replace("Eu sou o", "")
	if user_name.startswith("Eu sou a"):
		user_name = user_name.replace("Eu sou a", "")

	return user_name 


def  verifica_nome_exist(nome):
	dados = open("dados/nomes.txt", "r")
	nome_list = dados.readlines()

	if not nome_list:
		vazio = open("dados/nomes.txt", "r")
		conteudo = vazio.readlines()
		conteudo.append("{}".format(nome))
		vazio = open("dados/nomes.txt", "w")
		vazio.writelines(conteudo)
		vazio.close()

		return "Olá {}, prazer em te conhecer!".format(nome)

	for linha in nome_list:
		if linha == nome:
			return "Olá {}, Seja bem-vindo novamente".format(nome)

	vazio = open("dados/nomes.txt", "r")
	conteudo = vazio.readlines()
	conteudo.append("\n{}".format(nome))
	vazio = open("dados/nomes.txt", "w")
	vazio.writelines(conteudo)
	vazio.close()

	return "Oi {} é a primeira vez que nos falamos".format(nome)


def name_list():
	try:
		nomes = open("dados/nomes.txt", "r")
		nomes.close()

	except FileNotFoundError:
		nomes = open("dados/nomes.txt", "w")
		nomes.close()


#Definição para o clima
def clima_tempo():
	endereco_api = "http://api.openweathermap.org/data/2.5/weather?appid=78d740515eb1d6807ad36a52ba0dabf3&q="
	url = endereco_api + cidade

	infos = rq.get(url).json()

	longitude = infos['coord']['lon']
	latitude = infos['coord']['lat']

	temp = infos['main']['temp'] - 273.15 #Kelvin para Celsius
	pressao_atm = infos['main']['pressure'] / 1013.25 #Libras para ATM
	humidade = infos['main']['humidity'] #Porcentagem
	temp_max = infos['main']['temp_max'] - 273.15 #Kelvin para Celsius
	temp_min = infos['main']['temp_min'] - 273.15 #Kelvin para Celsius

	#Vento
	v_speed = infos['wind']['speed'] #Km/h
	v_direc = infos['wind']['deg'] #Recebe em graus

	#Nuvens
	nebulosidade = infos['clouds']['all']

	#id
	id_da_cidade = infos['id']

	return [longitude, latitude,
		 temp, pressao_atm, humidade,
		 temp_max, temp_min, v_speed,
		 v_direc, nebulosidade, id_da_cidade]

def temperatura():
	temp_atual = clima_tempo()[2]
	temp_max = clima_tempo()[5]
	temp_min = clima_tempo()[6]
	return [temp_atual, temp_max, temp_min]

def time():
	now = datetime.datetime.now()
	resposta = "São {} horas e {} minutos.".format(now.strftime("%H"), now.strftime("%M"))
	return resposta

def date():
	now = datetime.datetime.now()
	resposta = "Hoje é dia {} do {} de {}".format(now.day, now.strftime("%m"), now.year)
	return resposta

#def abrir():



	
