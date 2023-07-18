import speech_recognition as sr
import pyautogui
import pyaudio
from colorama import Fore, Style

# Criado um recognizer para reconhecer a fala
recognizer = sr.Recognizer()
# Criado um microfone para ouvir a fala
mic = sr.Microphone()
while True:
    print("LISTA DE COMANDOS: ")
    print(Fore.GREEN + "┌─────────────────────────────────────────────────────────────────┐")
    print(Fore.GREEN + "| ➡️ Nina - Inicia o script de manter o computador ligado         |")      
    print(Fore.GREEN + "| ➡️ Papa - Finaliza o script de manter o computador ligado       |")
    print(Fore.GREEN + "| ➡️ Stop - Finaliza o programa                                   |")
    print(Fore.GREEN + "| ➡️ Teams - Abre o Microsoft Teams                               |")
    print(Fore.GREEN + "| ➡️ Work Time - Abre o Visual Studio Code                        |")
    print(Fore.GREEN + "└─────────────────────────────────────────────────────────────────┘" + Style.RESET_ALL)
    with mic as source:
        print(Fore.RED + "\n🎤 ESPERANDO MENSAGEM...\n" + Style.RESET_ALL)
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    # Tenta reconhecer a fala
    try:
        # Passa o áudio para o reconhecedor de padroes do speech_recognition
        text = recognizer.recognize_google(audio)
        # Se a fala for reconhecida, apresenta o texto
        # print("You said: {}".format(text))

        # Se o texto dito for "Nina", inicia o script de manter o computador ligado
        if text == "Nina":
            print("✅ Recebido Nina! Iniciando o script de manter o computador ligado...")
            pyautogui.hotkey("win", "r")
            pyautogui.write("powershell -NoExit -Command \"$host.UI.RawUI.WindowTitle = 'Nina'; C:\\Users\\Gabriel_Stundner\\source\\repos\\GITHUB\\Jarbas\\runNoteAlive.bat\"")
            pyautogui.press("enter")
        
        # Se o texto dito for "Papa", finaliza o script de manter o computador ligado
        if text == "Papa":
            print("✅ Recebido Papa! Finalizando o script de manter o computador ligado...")
            pyautogui.hotkey("win", "r")
            pyautogui.write("powershell.exe Get-Process -Name \"notepad\" | Stop-Process -Force")
            pyautogui.press("enter")
            pyautogui.hotkey("win", "r")
            pyautogui.write("taskkill /fi \"WINDOWTITLE eq Nina\"")
            pyautogui.press("enter")
        
        # Se o texto dito for "stop", finaliza o programa
        if text == "stop":
            print("✅ Recebido Stop! Finalizando conexão...")
            pyautogui.hotkey("win", "r")
            pyautogui.write("powershell.exe Get-Process -Name \"WindowsTerminal\" | Stop-Process -Force")
            break

        # Se o texto for "work time", abre o visual studio code
        if text == "work time":
            print("✅ Recebido work time! Abrindo o Visual Studio Code...")
            pyautogui.hotkey("win", "r")
            pyautogui.write("code")
            pyautogui.press("enter")

        # Se o texto for "teams", abre o microsoft teams
        if text == "teams":
            print("✅ Recebido Teams! Abrindo o Microsoft Teams...")
            pyautogui.hotkey("win", "r")
            pyautogui.write("c:\\Users\\Gabriel_Stundner\\AppData\Roaming\\Microsoft\Windows\\Start Menu\\Programs\\Microsoft Teams (work or school).lnk")
            pyautogui.press("enter")

    except sr.UnknownValueError:
        print("Comando de voz não reconhecido. Reiniciando o programa...")
    except sr.RequestError as e:
        print("Não foi possível obter resultados; {0}".format(e))