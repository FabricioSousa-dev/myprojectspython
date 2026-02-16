import socket
import speedtest
import time

print("Iniciando teste............\n")
st = speedtest.Speedtest()
time.sleep(2)

print("Escolhendo o melhor servidor.......\n")
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


dowmload_mbps = download / 1_000_000
upload_mbps = upload / 1_000_000
time.sleep(5)

print("\n\n\n*******************Resultado do teste*************************\n\n")
print(f"Ping:{ping:.2f}ms")
print(f"Download:{dowmload_mbps:.2f} mps")
print(f"Upload:{upload_mbps:.2f} mbps")

print("****************************")
time.sleep(3)

print("\n\nTEstando conexão com a internet............")

print("Criar socket......")
sc = socket.socket()

print("\nMedir tempo.......")
tempo_inicial = time.time()

print("\nConectar.......")
connection = sc.connect(('www.google.com', 80))


tempo_final = time.time()
ping_socket = (tempo_final -tempo_inicial ) * 1000

print("\nconexão bem sucedida*****")
print(f"Ping (socket): {ping_socket:.2f} ms")

print("Fechar********")
sc.close()


