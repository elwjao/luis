import tkinter as tk
import random

# configurações
simbolos = ["🐂", "⭐", "🍊", "☕", "💀"]
saldo = 20.0
custo_giro = 2

animando = False

# animação com desaceleração
def animar_slots(rodadas=15, delay=50):
    global animando

    if rodadas > 0:
        temp = [random.choice(simbolos) for _ in range(3)]

        slot1.config(text=temp[0])
        slot2.config(text=temp[1])
        slot3.config(text=temp[2])

        # aumenta o delay → efeito de desacelerar
        janela.after(delay, animar_slots, rodadas - 1, delay + 15)
    else:
        animando = False

        resultado = resultado_final

        slot1.config(text=resultado[0])
        slot2.config(text=resultado[1])
        slot3.config(text=resultado[2])

        verificar_resultado(resultado)

# verificar resultado
def verificar_resultado(resultado):
    global saldo

    if resultado[0] == resultado[1] == resultado[2]:
        premio = 20
        saldo += premio
        resultado_label.config(text=f"🎉 JACKPOT! +R${premio}", fg="green")
    else:
        resultado_label.config(text="😕 Tente novamente...", fg="black")

    saldo_label.config(text=f"Saldo: R$ {saldo:.2f}")

# girar
def girar():
    global saldo, resultado_final, animando

    if animando:
        return

    if saldo < custo_giro:
        resultado_label.config(text="Saldo insuficiente!", fg="red")
        return

    saldo -= custo_giro
    saldo_label.config(text=f"Saldo: R$ {saldo:.2f}")

    resultado_final = [random.choice(simbolos) for _ in range(3)]

    animando = True
    animar_slots()

# janela
janela = tk.Tk()
janela.title("Slots")
janela.geometry("350x250")
janela.resizable(False, False)

titulo = tk.Label(janela, text="Cassino Senai", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

frame_slots = tk.Frame(janela)
frame_slots.pack(pady=10)

slot1 = tk.Label(frame_slots, text="❓", font=("Arial", 30))
slot1.pack(side="left", padx=10)

slot2 = tk.Label(frame_slots, text="❓", font=("Arial", 30))
slot2.pack(side="left", padx=10)

slot3 = tk.Label(frame_slots, text="❓", font=("Arial", 30))
slot3.pack(side="left", padx=10)

resultado_label = tk.Label(janela, text="Clique para girar", font=("Arial", 12))
resultado_label.pack(pady=10)

saldo_label = tk.Label(janela, text=f"Saldo: R$ {saldo:.2f}", font=("Arial", 12, "bold"))
saldo_label.pack()

botao = tk.Button(janela, text="Girar", font=("Arial", 12), command=girar)
botao.pack(pady=15)

janela.mainloop()