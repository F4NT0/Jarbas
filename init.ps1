# ----------------------------------------
# APRESENTAÇÃO INICIAL DO PROGRAMA JARBAS
# ----------------------------------------

# Variáveis
$EmojiIcon = [System.Convert]::toInt32("2705",16) # Emoji de check
$conteudo = Get-Content -Path "ascii.txt"

Write-Host ""

# Lendo as informações do arquivo ASCII
foreach ($linha in $conteudo) {
    Write-Host $linha
}

# Apresentando mensagem de boas vindas
Write-Host ""
Write-Host -ForegroundColor Green ([System.Char]::ConvertFromUtf32($EmojiIcon)) -NoNewline
Write-Host " INICIANDO PROGRAMA JARBAS..."
Write-Host ""

# Iniciando o programa
Start-Sleep -Seconds 2
cd C:\Users\Gabriel_Stundner\source\repos\GITHUB\Jarbas
pip install -q --disable-pip-version-check speechrecognition pyautogui pyaudio
python jarbas.py

# Finalizando o programa
Write-Host "Jarbas finalizado!"


