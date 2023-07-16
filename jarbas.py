import speech_recognition as sr
import pyautogui
import pyaudio

# Criado um recognizer para reconhecer a fala
recognizer = sr.Recognizer()
# Criado um microfone para ouvir a fala
mic = sr.Microphone()
# Ajusta o microfone para o ruído ambiente
while True:
    print("Lista de comandos ")
    print("Nina - Inicia o script de manter o computador ligado")
    print("Papa - Finaliza o script de manter o computador ligado")
    print("Stop - Finaliza o programa")
    print("Teams - Abre o Microsoft Teams")
    print("Work Time - Abre o Visual Studio Code")
    with mic as source:
        print("🎤 Ouvindo...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    # Tenta reconhecer a fala
    try:
        # Passa o áudio para o reconhecedor de padroes do speech_recognition
        text = recognizer.recognize_google(audio)
        # Se a fala for reconhecida, apresenta o texto
        print("You said: {}".format(text))

        # Se o texto dito for "Nina", inicia o script de manter o computador ligado
        if text == "Nina":
            print("✅ Recebido Nina! Iniciando o script de manter o computador ligado...")
            pyautogui.hotkey("win", "r")
            pyautogui.write("powershell.exe C:\\Users\\Gabriel_Stundner\\source\\repos\\GITHUB\\Jarbas\\runNoteAlive.bat")
            pyautogui.press("enter")
        
        # Se o texto dito for "Papa", finaliza o script de manter o computador ligado
        if text == "Papa":
            print("✅ Recebido Papa! Finalizando o script de manter o computador ligado...")
            pyautogui.hotkey("win", "r")
            pyautogui.write("powershell.exe Get-Process -Name \"notepad\" | Stop-Process -Force")
            pyautogui.press("enter")
            pyautogui.hotkey("win", "r")
            pyautogui.write("powershell.exe Get-Process -Name \"WindowsTerminal\" | Stop-Process -Force")
            pyautogui.press("enter")
        
        # Se o texto dito for "stop", finaliza o programa
        if text == "stop":
            print("✅ Recebido Stop! Finalizando conexão...")
            break

        # Se o texto for "teams", abre o microsoft teams
        if text == "work time":
            print("✅ Recebido Teams! Abrindo o Microsoft Teams...")
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