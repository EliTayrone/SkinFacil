import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

# Caminhões disponíveis
modelos_caminhoes = ["Scania", "Volvo", "Actros"]

# Caminho da imagem de fundo (ajustar se necessário)
IMAGEM_FUNDO = "tela_fundo.png"  # renomeie a imagem da Scania que você enviou para esse nome e coloque na pasta do projeto

class SkinFacilApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SkinFacil - Etapa 1")
        self.root.geometry("1024x600")
        self.root.resizable(False, False)

        # Carregar imagem de fundo
        if os.path.exists(IMAGEM_FUNDO):
            bg_image = Image.open(IMAGEM_FUNDO).resize((1024, 600))
            self.bg_photo = ImageTk.PhotoImage(bg_image)
            self.bg_label = tk.Label(root, image=self.bg_photo)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        else:
            self.bg_label = tk.Label(root, text="Imagem de fundo não encontrada", bg="gray", fg="white", font=("Arial", 16))
            self.bg_label.place(relx=0.5, rely=0.5, anchor="center")

        # Título
        titulo = tk.Label(root, text="Escolha o modelo do caminhão", font=("Arial", 16, "bold"), bg="#ffffff")
        titulo.place(x=30, y=20)

        # Combobox para seleção
        self.combo = ttk.Combobox(root, values=modelos_caminhoes, font=("Arial", 12))
        self.combo.place(x=30, y=60)
        self.combo.set("Selecione...")

        # Botão de confirmação
        self.botao_selecionar = tk.Button(root, text="Confirmar modelo", command=self.selecionar_modelo)
        self.botao_selecionar.place(x=30, y=100)

    def selecionar_modelo(self):
        modelo = self.combo.get()
        if modelo in modelos_caminhoes:
            print(f"Modelo selecionado: {modelo}")
            tk.messagebox.showinfo("Selecionado", f"Você escolheu: {modelo}")
        else:
            tk.messagebox.showwarning("Aviso", "Por favor, selecione um modelo válido.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SkinFacilApp(root)
    root.mainloop()
