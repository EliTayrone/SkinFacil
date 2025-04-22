
import tkinter as tk
from tkinter import filedialog, messagebox

def novo_projeto():
    messagebox.showinfo("Novo Projeto", "Novo projeto iniciado.")

def importar_template():
    file_path = filedialog.askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg")])
    if file_path:
        messagebox.showinfo("Importar Template", f"Template importado: {file_path}")

def exportar_mod():
    messagebox.showinfo("Exportar como .scs", "Exportação do mod simulada.")

app = tk.Tk()
app.title("SkinFacil - BY ELI TAYRONE")
app.geometry("800x600")

# Topo com botões
top_frame = tk.Frame(app)
top_frame.pack(pady=10)

btn_novo = tk.Button(top_frame, text="Novo Projeto", command=novo_projeto)
btn_novo.pack(side=tk.LEFT, padx=5)

btn_importar = tk.Button(top_frame, text="Importar Template", command=importar_template)
btn_importar.pack(side=tk.LEFT, padx=5)

btn_exportar = tk.Button(top_frame, text="Exportar como .scs", command=exportar_mod)
btn_exportar.pack(side=tk.LEFT, padx=5)

# Área de trabalho (futura área de colagem)
canvas = tk.Canvas(app, bg="lightgray", width=750, height=500)
canvas.pack(pady=20)

app.mainloop()
