from django import template
import json
import requests

register = template.Library()

@register.simple_tag 
def fx_rate(request):
    try:
        jsdata=requests.get('https://www.nbrb.by/api/exrates/rates/145')
        fx = jsdata.json()
        rate=fx.get('Cur_OfficialRate')
        date=fx.get('Date')[0:10]
        return f"{date} USD/BYN {rate} НБРБ"
    except:
        return "not available"
