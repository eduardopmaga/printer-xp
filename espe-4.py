from escpos.printer import Serial
from PIL import Image
import os

# Dados dos produtos e suas etiquetas
produtos = {
    "Eletron": ["path/to/etiqueta_x.png", "path/to/etiqueta_y.png", "path/to/etiqueta_z.png"],  # Substitua pelos caminhos das suas etiquetas
    "Produto_B": ["path/to/etiqueta_a.png", "path/to/etiqueta_b.png"],
    "Produto_C": ["path/to/etiqueta_c.png", "path/to/etiqueta_d.png", "path/to/etiqueta_e.png"],
}

# Configurações da impressora USB
SERIAL_PORT = 'COM3'  # Substitua pela sua porta de impressora
BAUDRATE = 9600  # Ajuste se necessário

# Função para imprimir etiquetas
def print_labels(labels):
    try:
        # Conectar à impressora
        p = Serial(SERIAL_PORT, baudrate=BAUDRATE)
        for label in labels:
            if os.path.exists(label):
                image = Image.open(label)
                p.image(image)  # Enviar imagem para a impressora
                p.cut()  # Cortar após imprimir cada etiqueta
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
