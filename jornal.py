import requests
import json
import pandas as pd
import os
os.system('cls' if os.name == 'nt' else 'clear')

def exportar_csv(titulo, link, nome):
	df = pd.DataFrame({'Títulos': titulo, 'Link': link})
	df.to_csv('%s.csv' % nome, index=False, sep=';', encoding='utf-8-sig')
	print('\nArquivo exportado com sucesso para a pasta do projeto!\n')

def buscar_noticias(dados):
	titulo = []
	link = []
	for p in dados["response"]["results"]:
		titulo.append(p['webTitle'])
		link.append(p['webUrl'])
	exportar_csv(titulo, link, "noticias")

def buscar_sports(dados):
	titulo = []
	link = []
	for p in dados["response"]["results"]:
		if p["pillarName"] == "Sport":
			titulo.append(p["webTitle"])
			link.append(p["webUrl"])
	if len(titulo) == 0:
		print("\nNão foi encontrada nenhuma noticia. Tente mais tarde!\n")
	else:
		exportar_csv(titulo, link, "sports")
	

def buscar_news(dados):
	titulo = []
	link = []
	for p in dados["response"]["results"]:
		if p["pillarName"] == "News":
			titulo.append(p["webTitle"])
			link.append(p["webUrl"])
	if len(titulo) == 0:
		print("\nNão foi encontrada nenhuma noticia. Tente mais tarde!\n")
	else:
		exportar_csv(titulo, link, "news")

def buscar_arts(dados):
	titulo = []
	link = []
	for p in dados["response"]["results"]:
		if p["pillarName"] == "Arts":
			titulo.append(p["webTitle"])
			link.append(p["webUrl"])
	if len(titulo) == 0:
		print("\nNão foi encontrada nenhuma noticia. Tente mais tarde!\n")
	else:
		exportar_csv(titulo, link, "artes")

def main():

	url = "https://content.guardianapis.com/search?api-key=c99d706c-1e4b-4a87-b4ab-fbb222c6063d"
	response = requests.get(url)
	if response.status_code == 200:
		print("\nAcessando a Base de Dados do The Guardian...\n")
		dados = response.json()
		escolha = 4
		while escolha != 0:
			print("1 - Esportes")
			print("2 - Notícias")
			print("3 - Artes")
			print("4 - Todas")
			print("0 - para Sair")
			try:
				opcao = int(input("\nDigite o Número referente as Notícias que você quer baixar: "))
			except:
				print("Digite apenas números")
			if opcao > 4:
				print("\nPor Favor digite números entre 0 e 4!\n")
			elif opcao < 0:
				print("\nPor Favor digite números entre 0 e 4!\n")
			elif opcao == 1:
				buscar_sports(dados)
			elif opcao == 2:
				buscar_news(dados)
			elif opcao == 3:
				buscar_arts(dados)
			elif opcao == 4:
				buscar_noticias(dados)
			elif opcao == 0:
				print("\nObrigado por Utilizar o Programa!\n")
				break
	else:
		print("\nNão foi possível acessar a base de dados\n")



if __name__ == "__main__":
	main()