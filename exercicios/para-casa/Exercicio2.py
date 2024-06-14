arquivo_download=float(input("Informe o tamanho do arquivo baixado"))
velocidade_internet=float(input("Informe a velocidade da sua internet"))
download_segundos=arquivo_download/velocidade_internet
tempo_aproximado=download_segundos/60
print(f"Seu tempo aproximado em segundos é {download_segundos}")
print(f"O tempo aproximado de download é de {tempo_aproximado} minutos")