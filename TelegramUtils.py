#!/opt/rh/rh-python36/root/usr/bin/python3
import logging
import requests

logging.basicConfig(filename="bot.log", filemode="w", level=logging.INFO, format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def sendMessage(message):
    bot_token = 'bot819737990:AAGeCu9U3TEjTzTWABp9lwsotnRJzKvBoLM'
    bot_chat_id = '-329721137'
    parse_mode = 'Markdown'
    api_url = 'https://api.telegram.org/'
    request_url = api_url + bot_token + '/sendMessage?chat_id=' + bot_chat_id + '&parse_mode=' + parse_mode + '&text=' + message
    response = requests.post(request_url)
    logging.info(response.json())
