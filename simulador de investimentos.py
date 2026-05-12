import tkinter as tk

root = tk.Tk()
root.title("Simulador de investimentos - Sicredi ")
root.geometry("330x580")
root.configure(bg="#820AD1")
root.resizable(width=False, height=False)


#titulo
titulo = tk.Label(root,
         text= "=== banco de investimentos NU ===",
font=("Arial", 12, "bold"),
bg="#820AD1", 
fg="white"
)
titulo.pack(pady=(20, 10))

#valor inicial
valor_inicial_label = tk.Label(root,#criando o label para o valor inicial
         text= "Valor inicial(R$):", # texto do label
font=("Arial", 10), #fonte do texto
bg="#820AD1", #cor de fundo do label
fg="white"#cor do texto do label
)
valor_inicial_label.pack(pady=(10, 5))

entrada_texto = tk.Entry(root, font=("Arial", 10))
entrada_texto.pack(pady=(0, 10))#configurando a cor de fundo e do texto da caixa de entrada
entrada_texto.configure(bg="white", fg="black")

root.mainloop()