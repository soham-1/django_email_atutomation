import requests
import traceback

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (From, To, PlainTextContent, HtmlContent, Mail)

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

    res_weather = data['weather'][0]['main'].lower()
    if res_weather in weather_emoticons:
        emoticon = weather_emoticons[res_weather]

    sendgrid_client = SendGridAPIClient(api_key=secrets.SENDGRID_API_KEY)
    from_email = From(secrets.EMAIL_HOST_USER)
    to_email = To(instance.email)
    subject = "Hi " + instance.name + ", interested in our services"
    plain_text_content = PlainTextContent(
        f"The current temperature in {instance.city} is {data['main']['temp']} C {emoticon}"
    )
    message = Mail(from_email, to_email, subject, plain_text_content)
    response = sendgrid_client.send(message=message)
    print(response)
    return
