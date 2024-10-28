import usb.core
import usb.util
import os

# Dados dos produtos e suas etiquetas
produtos = {
    "a": ["etiquetas/Etiq. Carr.Fonte.axp", "etiquetas/Etiq. Carreg.Car CAIXA NOVA.axp", "etiquetas/Etiq. P001.axp"],  # Substitua pelos caminhos das suas etiquetas
}

# Função para enviar comandos diretos para a impressora Argox usando protocolo PPLA/PPLB
def send_to_printer(command):
    try:
        # Conectar à impressora Argox OS-214 (ajuste os valores de idVendor e idProduct)
        dev = usb.core.find(idVendor=0x403, idProduct=0xA8B0)  # Certifique-se de que esses IDs estão corretos

        if dev is None:
            raise ValueError("Impressora não encontrada.")

        # Configurar dispositivo
        dev.set_configuration()
        cfg = dev.get_active_configuration()
        intf = cfg[(0, 0)]

        # Encontrar o endpoint correto
        ep = usb.util.find_descriptor(
            intf,
            custom_match=lambda e: usb.util.endpoint_direction(e.bEndpointAddress) == usb.util.ENDPOINT_OUT
        )

        if ep is None:
            raise ValueError("Endpoint de saída não encontrado.")

        # Enviar comando para a impressora
        ep.write(command.encode('utf-8'))

    except Exception as e:
        print(f"Erro ao enviar para a impressora: {e}")

# Função para imprimir etiquetas
def print_labels(labels):
    try:
        for label in labels:
            if os.path.exists(label):
                # Lógica de processamento da etiqueta e comando PPLA/PPLB correspondente
                # Exemplo simples de comando PPLA para imprimir uma etiqueta de texto:
                command = f"""
                ! 0 200 200 210 1
                TEXT 4 0 30 40 {label}
                PRINT
                """
                send_to_printer(command)
            else:
                print(f"Etiqueta não encontrada: {label}")
    except Exception as e:
        print(f"Erro ao imprimir: {e}")

# Função principal para interagir no terminal
def main():
    print("Impressão de Etiquetas")
    codigo_produto = input("Digite o código do produto: ")

    if codigo_produto in produtos:
        labels = produtos[codigo_produto]  # Obtém as etiquetas relacionadas ao produto
        print_labels(labels)  # Imprimir as etiquetas
        print("Etiquetas enviadas para impressão.")
    else:
        print("Código do produto não encontrado.")

if __name__ == "__main__":
    main()
