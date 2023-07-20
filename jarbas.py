import speech_recognition as sr
import pyautogui
import winsound
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
    print(Fore.GREEN + "| ➡️ Work Time - Abre o Microsoft Teams                           |")
    print(Fore.GREEN + "| ➡️ Developer - Abre o Visual Studio Code                        |")
    print(Fore.GREEN + "| ➡️ Internet - Abre o navegador                                  |")
    print(Fore.GREEN + "| ➡️ Design - Abre o programa de design                           |")
    print(Fore.GREEN + "| ➡️ Record - Abre o programa de gravação                         |")
    print(Fore.GREEN + "| ➡️ Picture - Tira um screenshot                                 |")
    print(Fore.GREEN + "| ➡️ Clock Time - Abre o programa de controle de horas            |")
    print(Fore.GREEN + "| ➡️ Shutdown - Desliga o computador                              |")
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
        print("You said: {}".format(text))

        # Se o texto dito for "Nina", inicia o script de manter o computador ligado
        if "Nina" in text:
            winsound.Beep(400,1000)
            print("✅ Recebido Nina! Iniciando o script de manter o computador ligado...")
            pyautogui.hotkey("win", "r")
            pyautogui.write("powershell.exe -NoLogo -NoExit -Command \"$host.UI.RawUI.WindowTitle = 'Nina'; C:\\Users\\Gabriel_Stundner\\source\\repos\\GITHUB\\Jarbas\\runNoteAlive.bat\"")
            pyautogui.press("enter")
        
        # Se o texto dito for "Papa", finaliza o script de manter o computador ligado
        if "papa" in text:
            winsound.Beep(400,1000)
            print("✅ Recebido Papa! Finalizando o script de manter o computador ligado...")
            pyautogui.hotkey("win", "r")
            pyautogui.write("powershell.exe Get-Process -Name \"notepad\" | Stop-Process -Force")
            pyautogui.press("enter")
            pyautogui.hotkey("win", "r")
            pyautogui.write("taskkill /fi \"WINDOWTITLE eq Nina\"")
            pyautogui.press("enter")
        
        # Se o texto dito for "stop", finaliza o programa
        if "stop" in text:
            winsound.Beep(400,1000)
            print("✅ Recebido Stop! Finalizando conexão...")
            pyautogui.hotkey("win", "r")
            pyautogui.write("powershell.exe Get-Process -Name \"WindowsTerminal\" | Stop-Process -Force")
            pyautogui.press("enter")
            break

        # Se o texto for "developer", abre o visual studio code
        if "developer" in text:
            winsound.Beep(400,1000)
            print("✅ Recebido Developer! Abrindo o Visual Studio Code...")
            pyautogui.hotkey("win", "r")
            pyautogui.write("code")
            pyautogui.press("enter")

        # Se o texto for "work time", abre o microsoft teams
        if "work time" in text:
            winsound.Beep(400,1000)
            print("✅ Recebido Work Time! Abrindo o Microsoft Teams...")
            pyautogui.hotkey("win", "r")
            pyautogui.write("c:\\Users\\Gabriel_Stundner\\AppData\Roaming\\Microsoft\Windows\\Start Menu\\Programs\\Microsoft Teams (work or school).lnk")
            pyautogui.press("enter")
        
        # Se o texto for "shutdown", desliga o computador
        if "shut down" in text:
            winsound.Beep(400,1000)
            print("✅ Recebido shutdown! Desligando o computador...")
            pyautogui.hotkey("win", "r")
            pyautogui.write("shutdown /s")
            pyautogui.press("enter")
        
        # Se o texto for "internet", abre o navegador
        if "internet" in text:
            winsound.Beep(400,1000)
            print("✅ Recebido internet! Abrindo o navegador...")
            pyautogui.hotkey("win", "r")
            pyautogui.write("msedge")
            pyautogui.press("enter")
        
        # Se o texto for "clock time", abre o programa de controle de horas
        if "clock time" in text:
            winsound.Beep(400,1000)
            print("✅ Recebido clock time! Abrindo o programa de controle de horas...")
            pyautogui.hotkey("win", "r")
            pyautogui.write("wt Powershell.exe -NoLogo -NoExit -Command \"$host.UI.RawUI.WindowTitle = 'Clock Time' \; C:\\Users\\Gabriel_Stundner\\source\\repos\\GITHUB\\Controle_Horas\\ControleHoras.ps1\"")
            pyautogui.press("enter")
        
        if "design" in text:
            winsound.Beep(400,1000)
            print("✅ Recebido design! Abrindo o programa de design...")
            pyautogui.hotkey("win", "r")
            pyautogui.write("C:\\Users\\Gabriel_Stundner\\AppData\\Local\\Programs\\Canva\\Canva.exe")
            pyautogui.press("enter")
        
        if "record" in text:
            winsound.Beep(400,1000)
            print("✅ Recebido record! Abrindo o programa de gravação...")
            pyautogui.hotkey("win", "r")
            pyautogui.write("C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe")
            pyautogui.press("enter")
        
        if "picture" in text:
            winsound.Beep(400,1000)
            print("✅ Recebido picture! Abrindo o programa de screenshot...")
            pyautogui.press("printscreen")


    except sr.UnknownValueError:
        print("Comando de voz não reconhecido. Reiniciando o programa...")
    except sr.RequestError as e:
        print("Não foi possível obter resultados; {0}".format(e))