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
opload_mbps = upload / 1_000_000

print("\n\n\n*******************Resultado do teste*************************\n\n")
print(f"Ping:{ping:.2f}ms")
print(f"Download:{dowmload_mbps:.2f}mps")
print(f"Upload:{upload:.2f}mbps")

print("****************************")

