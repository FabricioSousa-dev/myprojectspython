import socket
import speedtest
import time
import emoji

print(emoji.emojize("Iniciando teste:globe_with_meridians:............\n"))
st = speedtest.Speedtest()
time.sleep(2)

print(emoji.emojize("Escolhendo o melhor servidor:satellite_antenna:\n"))
st.get_best_server()
time.sleep(2)

print("Testando o ping.......\n")
ping = st.results.ping
time.sleep(2)

print("Testar download.......\n")
download = st.download()
time.sleep(2)

print("Testar upload.......\n")
upload = st.upload()
time.sleep(2)


download_mbps = download / 1_000_000
upload_mbps = upload / 1_000_000
time.sleep(5)

print("\n\n\n*******************Resultado do teste*************************\n\n")
print(f"Ping:{ping:.2f}ms")
print(f"Download:{download_mbps:.2f} mbps")
print(f"Upload:{upload_mbps:.2f} mbps")

print("****************************")
time.sleep(3)

print(emoji.emojize("\n\nTestando conexão com a internet:globe_with_meridians:............"))

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

print("*************Fechar********")
sc.close()


