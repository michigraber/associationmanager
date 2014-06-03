'''
Populate the database with IKEDA SEMINAR 2014 events DATA
'''

from datetime import date, datetime

from events.models import Event, EventPart, Article


EVENT = {
        'title_en': 'Hiroshi Ikeda Shihan 2014', 
        'title_de': 'Hiroshi Ikeda Shihan 2014',

        'date_from': date(2014, 07, 25),
        'date_until': date(2014, 07, 27),

        'slug': 'hiroshi-ikeda-shihan-2014',
        
        'show_event': True,
        }

EVENT_PARTS = [
        {
            'datetime_from': datetime(2014, 07, 25, 19, 00, 00),
            'datetime_until': datetime(2014, 07, 25, 21, 00, 00),

            'short_description_de': 'Keiko Freitag Abend',
            'short_description_en': 'Keiko Friday Evening',

            'is_bookable': True,
            'max_no_participants': 50,
            },
        {
            'datetime_from': datetime(2014, 07, 26, 10, 00, 00),
            'datetime_until': datetime(2014, 07, 26, 12, 00, 00),

            'short_description_de': 'Keiko Samstag Morgen',
            'short_description_en': 'Keiko Saturday Morning',

            'is_bookable': True,
            'max_no_participants': 120,
            },
        {
            'datetime_from': datetime(2014, 07, 26, 15, 00, 00),
            'datetime_until': datetime(2014, 07, 26, 17, 00, 00),

            'short_description_de': 'Keiko Samstag Nachmittag',
            'short_description_en': 'Keiko Saturday Afternoon',

            'is_bookable': True,
            'max_no_participants': 120,
            },
        {
            'datetime_from': datetime(2014, 07, 27, 10, 00, 00),
            'datetime_until': datetime(2014, 07, 27, 12, 00, 00),

            'short_description_de': 'Keiko Sonntag Morgen',
            'short_description_en': 'Keiko Sunday Morning',

            'is_bookable': True,
            'max_no_participants': 120,
            },
        {
            'datetime_from': datetime(2014, 07, 27, 14, 00, 00),
            'datetime_until': datetime(2014, 07, 27, 16, 00, 00),

            'short_description_de': 'Keiko Sonntag Nachmittag',
            'short_description_en': 'Keiko Sunday Afternoon',

            'is_bookable': True,
            'max_no_participants': 120,
            },
        ]

ARTICLES = [
        {
            'name_de': 'Party Samstag Abend',
            'name_en': 'Party Saturday Evening',

            'price': 10,
            'no_articles_initially': 120,
            },
        ]


def populate_database():

    event, created = Event.objects.get_or_create(**EVENT)
    event.save()

    for EP in EVENT_PARTS:
        ep, created = EventPart.objects.get_or_create(event=event, **EP)
        ep.save()

    for ART in ARTICLES:
        art, created = Article.objects.get_or_create(**ART)
        art.save()
        art.events.add(event)
        art.save()
