# HeartBeat
Confere quanto tempo raspberry não manda sinal de vida

hospedado em: http://willianchan.pythonanywhere.com/

para mandar sinal de vida, raspberry deve mandar GET num intervalo de 1 em 1 minuto em: http://willianchan.pythonanywhere.com/estouvivo

Raspberry está rodando código send_heart_beat.py desde quando liga.


Para configurar o raspberry para rodar o algoritmo ao iniciar...

abra o arquivo de configuração do crontab
```bash
crontab -e
```

adicione a seguinte linha:
@reboot python3 /home/pi/send_heart_beat.py
