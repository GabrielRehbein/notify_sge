import requests
from django.conf import settings


class CallMeBot:

    def __init__(self):
        self.__base_url = 'https://api.callmebot.com/whatsapp.php'
        self.__api_key = settings.CALLMEBOT_API_KEY
        self.__phone = settings.CALLMEBOT_PHONE_NUMBER

    def whatsapp_message(self, content):
        url = f'{self.__base_url}?phone=+{self.__phone}&text={content}&apikey={self.__api_key}'
        response = requests.get(url=url)