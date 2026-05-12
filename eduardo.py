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
            print("Sistema Operacional não reconhecido.")

    except Exception as e:
        print(f"Erro: {e}")

# Chama a função
shutdown()