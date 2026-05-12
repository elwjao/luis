import time
import sys
import os
import platform

def shutdown():
    sistema = platform.system().lower()

    try:
        if "windows" in sistema:
            os.system("shutdown /s /t 0")
        elif "linux" in sistema or "darwin" in sistema:
            os.system("shutdown now")
        else:
            print("SISTEMA OPERACIONAL NÃO RECONHECIDO")

    except Exception as e:
        print(f"Erro ao tentar o shutdown")

def temporizador_em_shutdown():
    segundos = int(input())

    while segundos > 0:
        mins, secs = divmod(segundos, 60)
        timer = f"{mins:02d}:{secs:02d}"

        # Pisca a cada 10 segundos
        if segundos % 10 == 0:
            print(f"Tempo restante: {timer}", end="\r", flush=True)

        time.sleep(1)
        segundos -= 1

    print("\nIniciando desligamento... Tchau! 👋")

    shutdown()

try:
    print("Pronto por favor digite apenas números inteiros")

    temporizador_em_shutdown()

except ValueError:
    print("Por favor digite apenas números inteiros")

except KeyboardInterrupt:
    print("\nPrograma cancelado pelo usuário.")