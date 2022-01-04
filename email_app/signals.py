import requests
import traceback

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

from .models import EmailModel
from .env import secrets

@receiver(post_save, sender=EmailModel)
def send_gmail(sender, instance, **kwargs):
    payload = {'q': instance.city, 'appid': secrets.API_KEY, 'units': 'metric'}
    res = requests.get("https://api.openweathermap.org/data/2.5/weather", params=payload)
    data = res.json()
    print(data)
    if data['cod'] == 404:
        print("invalid request")
        return

    # smoke haze sun wind snow rain
    emoticon = "\N{sun with face}" # default to sun emoji
    weather_emoticons = {
        'rain': "\N{cloud with rain}",
        'wind': "\U0001F32A",
        "haze": "\N{sun behind cloud}",
        "smoke": "\N{fog}",
        "snow": "\N{snowflake}"
    }
    
    try:
        res_weather = data['weather'][0]['main'].lower()
        if res_weather in weather_emoticons:
            emoticon = weather_emoticons[res_weather]

        message = f"The current temperature in {instance.city} is {data['main']['temp']} C {emoticon}"
        subject = "Hi " + instance.name + ", interested in our services"
        send_mail(subject, message, settings.EMAIL_HOST_USER, [instance.email], fail_silently=False)
    except Exception as e:
        print(traceback.format_exc())
