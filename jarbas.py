import speech_recognition as sr
import pyautogui
import pyaudio

# Criado um recognizer para reconhecer a fala
recognizer = sr.Recognizer()
# Criado um microfone para ouvir a fala
mic = sr.Microphone()
# Ajusta o microfone para o ruído ambiente
while True:
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
        if text == "stop":
            print("✅ Recebido Stop! Finalizando conexão...")
            break
    except sr.UnknownValueError:
        print("Eu não entendi o que você disse. Finalizando conexão...")
    except sr.RequestError as e:
        print("Não foi possível obter resultados; {0}".format(e))