import socket
import speedtest
import time
import emoji

print(emoji.emojize("Iniciando teste:globe_with_meridians:............\n"))
time.sleep(4)
st = speedtest.Speedtest()


print(emoji.emojize("Escolhendo o melhor servidor:satellite_antenna:\n"))
st.get_best_server()


print("Testando o ping.......\n")
ping = st.results.ping


print("Testar download.......\n")
download = st.download()


print("Testar upload.......\n")
upload = st.upload()



download_mbps = download / 1_000_000
upload_mbps = upload / 1_000_000

print("\n\n*******************Resultado do teste*************************\n")
print(f"Ping:{ping:.2f}ms")
print(f"Download:{download_mbps:.2f} mbps")
print(f"Upload:{upload_mbps:.2f} mbps")

print("****************************")
time.sleep(5)

print(emoji.emojize("\n\n************Testando conexão com a internet:globe_with_meridians:............"))

print("Criar socket......")
sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("\nMedir tempo.......")
tempo_inicial = time.time()

print("\nConectar.......")
connection = sc.connect(('www.google.com', 80))


tempo_final = time.time()
ping_socket = (tempo_final -tempo_inicial ) * 1000

print("\nconexão bem sucedida*****")
print(f"Ping (socket): {ping_socket:.2f} ms")

print("\n\n******Fechando conexão********")
sc.close()

print("\n\nFuncionou até aqui,obrigado pela paciência!")
print("Até mais!")

