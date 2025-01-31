import os
import pyaes
import tkinter as tk
from tkinter import filedialog

# Criar uma janela oculta do Tkinter
root = tk.Tk()
root.withdraw()

# Abrir um diálogo para selecionar um arquivo criptografado
file_path = filedialog.askopenfilename(title="Selecione um arquivo para descriptografar")

# Verifica se o usuário selecionou um arquivo
if file_path:
    # Ler o arquivo criptografado
    with open(file_path, "rb") as file:
        file_data = file.read()
    
    # Definir a chave de descriptografia
    key = b"testeransomwares"
    aes = pyaes.AESModeOfOperationCTR(key)
    
    # Descriptografar os dados
    decrypt_data = aes.decrypt(file_data)
    
    # Remover o arquivo criptografado
    os.remove(file_path)
    
    # Criar o novo nome do arquivo descriptografado
    new_file_path = file_path.replace(".ransomwaretroll", "")
    
    # Salvar o arquivo descriptografado
    with open(new_file_path, "wb") as new_file:
        new_file.write(decrypt_data)
    
    print(f"Arquivo descriptografado salvo como: {new_file_path}")
else:
    print("Nenhum arquivo foi selecionado.")
