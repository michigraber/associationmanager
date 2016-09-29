import random
from django.shortcuts import render_to_response

def memory(request, language=''):

    ROW_LENGTH = 5 

    friday_no_imgs = 70
    rows = []
    row = []
    
    for i in range(1, friday_no_imgs+1):
        if len(row) % ROW_LENGTH == 0:
            row = []
        if i < 10:
            strnum = '0'+str(i)
        else:
            strnum = str(i)
        row.append(strnum)
        if len(row) == ROW_LENGTH:
            rows.append(row)

    albums = [
            {
                'name_de' : 'Ikeda Seminar Z&uuml;rich 2014 - Freitag',
                'name_en' : 'Ikeda Seminar Z&uuml;rich 2014 - Friday',
                'prefix' : 'IkedaZurich2014Friday', 
                'rows': rows,
                }
            ]

    ddict = { 
            'language': language,
            'albums': albums,
            }
    return render_to_response('memory.html', ddict )


def welcome(request, language=''):
    ddict = { 
            'language': language,
            'image_nr': str(int(round(random.random()))),
            }
    return render_to_response('welcome.html', ddict )


def registration(request, language='de'):
    ddict = { 
            'language': language,
            'reason': 'end',
            }
    return render_to_response('registration_offline.html', ddict )
