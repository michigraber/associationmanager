import random
from django.shortcuts import render_to_response


def welcome(request, language=''):
    ddict = { 
            'language': language,
            'image_nr': str(int(round(random.random()))),
            }
    return render_to_response('welcome.html', ddict )


def registration(request, lang='de'):
    ddict = { 
            'language': lang,
            }
    return render_to_response('registration.html', ddict )
