import etcd3
import time

client = etcd3.client(host='172.21.0.10', port=2379)

def update_counter () :
    current_counter_bytes, _ = client.get('/counter')
    current_counter = int(current_counter_bytes.decode('utf-8')) if current_counter_bytes else 0

    # Incrementa
    new_value = current_counter + 1

    # Salva o novo valor no etcd
    client.put('/counter', str(new_value))

    print(f"Contador atualizado de {current_counter} para: {new_value} (Timestamp: {time.time()})")
    return new_value


if __name__ == "__main__":
    print(f"Iniciando serviço de contador lógico")
    try:
        while True:
            update_counter()
            time.sleep(5) # Espera 2 segundos antes da próxima atualização
    except KeyboardInterrupt:
        print(f"Serviço de contador lógico interrompido.")