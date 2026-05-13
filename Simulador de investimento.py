import tkinter as tk

root = tk.Tk()
root.title("Nubank") #titulo da janela
root.geometry("600x600")#dimensões da janela
root.configure(bg="#820AD1")#cor de fundo da janela
root.resizable(width=False, height=False)#impede o redimensionamento da janela


#titulo
titulo = tk.Label(root,
         text= "Nubank ",
font=("Arial", 40, "bold"),
bg="#820AD1", 
fg="white"
)
titulo.pack(pady=(20, 10))

#valor inicial
valor_inicial_label = tk.Label(root,#criando o label para o valor inicial
         text= "Valor inicial(R$):", # texto do label
font=("Arial", 25), #fonte do texto
bg="#820AD1", #cor de fundo do label
fg="white"#cor do texto do label
)
valor_inicial_label.pack(pady=(10, 5))#configurando o espaçamento entre o label e a caixa de entrada

entrada_texto = tk.Entry(root, font=("Arial", 20))
entrada_texto.pack(pady=(0, 10))#configurando a cor de fundo e do texto da caixa de entrada
entrada_texto.configure(bg="white", fg="black")



taxa_juros_label = tk.Label(root,
            text= "Taxa de juros mensal(%):", # texto do label
font=("Arial", 25), #fonte do texto
bg="#820AD1", #cor de fundo do label
fg="white"#cor do texto do label
)
taxa_juros_label.pack(pady=(10, 5))#configurando o espaçamento entre o label e a caixa de entrada
entrada_taxa_juros = tk.Entry(root, font=("Arial", 20))
entrada_taxa_juros.pack(pady=(0, 10))#configurando a cor de fundo e do texto da caixa de entrada
entrada_taxa_juros.configure(bg="white", fg="black")

periodo_label = tk.Label(root,
            text= "Período(meses):", # texto do label
font=("Arial", 25), #fonte do texto
bg="#820AD1", #cor de fundo do label
fg="white"#cor do texto do label
)
periodo_label.pack(pady=(10, 5))#configurando o espaçamento entre o label e a caixa de entrada
entrada_periodo = tk.Entry(root, font=("Arial", 20))
entrada_periodo.pack(pady=(0, 10))#configurando a cor de fundo e do texto da caixa de entrada
entrada_periodo.configure(bg="white", fg="black")

resultado_label = tk.Label(
    root,
    text="Valor final aparecerá aqui",
    font=("Arial", 20),
    bg="#820AD1",
    fg="white"
)

resultado_label.pack(pady=(10, 10))
resultado_label.pack(pady=(10, 5))#configurando o espaçamento entre o label e a caixa de entrada


def calcular_investimento():
    try:
        valor_inicial = float(entrada_texto.get())
        taxa_juros = float(entrada_taxa_juros.get()) / 100
        periodo = int(entrada_periodo.get())

        valor_final = valor_inicial * (1 + taxa_juros) ** periodo

        resultado_label.config(
            text=f"Valor final: R$ {valor_final:.2f}"
        )

    except ValueError:
        resultado_label.config(text="Entrada inválida")

# botão para calcular o investimento
botao_calcular = tk.Button(
    root,
    text="Calcular",
    command=calcular_investimento,
    font=("Arial", 20, "bold"), # aumenta o texto
    width=10,  # largura do botão
    height=1,  # altura do botão
    bg="white",
    fg="#820AD1"
)

botao_calcular.pack(pady=(10, 0))

root.mainloop()