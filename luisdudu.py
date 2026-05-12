import tkinter as tk 
import random 

#configurações 
simbolos = ["🐂", "⭐", "🍊","☕","💀"]
saldo=20.0
custo_giro=2
#função girar

def girar():
    global saldo

    if saldo < custo_giro:
        resultado_label.config(text="saldo insuficiente!", fg="red")
        return

    saldo -= custo_giro

    resultado = [random.choice(simbolos) for _ in range(3)]

    slot1.config(text=resultado[0])
    slot2.config(text=resultado[1])
    slot3.config(text=resultado[2])

    if resultado[0] == resultado[1] == resultado[2]:
        premio = 20
        saldo += premio
        resultado_label.config(text=f"🎉 JACKPOT! +R${premio}", fg="green")
    else:
        resultado_label.config(text="😕 tente novamente...", fg="black")

    saldo_label.config(text=f"Saldo: R${saldo:.2f}")

#janela Principal

janela = tk.Tk()
janela.title("Slots")
janela.geometry("350x250")
janela.resizable(False,False)

#titulo
titulo = tk.label(janela, text="Cassino senai",
fonte=("Arial",16, "Bold")) 
titulo.pack(pady=10)

#frame dos slots

frame_slots = tk.Frame(janela)
frame_slots.pack(pady=10)

slot1 = tk.Label(frame_slots, text="❓", font=("Arial,30"))
slot1.pack(side="left", padx=10)

slot2 = tk.Label(frame_slots, text="❓", font=("Arial,30"))
slot2.pack(side="left", padx=10)

slot3 = tk.Label(frame_slots, text="❓", font=("Arial,30"))
slot3.pack(side="left", padx=10)

#resultado

resultado_Label = tk.label(janela, text= " Clique para girar", font=("Arial", 12))
resultado_Label.pack(pady=10)

#saldo

saldo_label = tk.label(janela, text=f"saldo: R$ {saldo:.2f}", font=("Arial", 12, "Bold"))

#botao girar
botao = tk.button(janela, text=("Arial", 12), comand=girar)
botao.pack(pady=15)

# loop 
janela.mainloop()