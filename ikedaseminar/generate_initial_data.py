'''
Populate the database with IKEDA SEMINAR 2018 events DATA
'''

from datetime import date, datetime

from events.models import Event, EventPart, Article


EVENT = {
        'title_en': 'Hiroshi Ikeda Shihan 2018', 
        'title_de': 'Hiroshi Ikeda Shihan 2018',

        'date_from': date(2018, 10, 5),
        'date_until': date(2018, 10, 7),

        'slug': 'hiroshi-ikeda-shihan-2018',
        
        'show_event': True,
        }

EVENT_PARTS = [
        {
            'datetime_from': datetime(2018, 10, 5, 19, 00, 00),
            'datetime_until': datetime(2018, 10, 5, 21, 00, 00),

            'short_description_de': 'Keiko Freitag Abend',
            'short_description_en': 'Keiko Friday Evening',

            'is_bookable': True,
            'max_no_participants': 60,
            },
        {
            'datetime_from': datetime(2018, 10, 6, 10, 00, 00),
            'datetime_until': datetime(2018, 10, 6, 12, 00, 00),

            'short_description_de': 'Keiko Samstag Morgen',
            'short_description_en': 'Keiko Saturday Morning',

            'is_bookable': True,
            'max_no_participants': 60,
            },
        {
            'datetime_from': datetime(2018, 10, 6, 15, 00, 00),
            'datetime_until': datetime(2018, 10, 6, 17, 00, 00),

            'short_description_de': 'Keiko Samstag Nachmittag',
            'short_description_en': 'Keiko Saturday Afternoon',

            'is_bookable': True,
            'max_no_participants': 60,
            },
        {
            'datetime_from': datetime(2018, 10, 7, 10, 00, 00),
            'datetime_until': datetime(2018, 10, 7, 12, 00, 00),

            'short_description_de': 'Keiko Sonntag Morgen',
            'short_description_en': 'Keiko Sunday Morning',

            'is_bookable': True,
            'max_no_participants': 60,
            },
        {
            'datetime_from': datetime(2018, 10, 7, 14, 00, 00),
            'datetime_until': datetime(2018, 10, 7, 16, 00, 00),

            'short_description_de': 'Keiko Sonntag Nachmittag',
            'short_description_en': 'Keiko Sunday Afternoon',

            'is_bookable': True,
            'max_no_participants': 60,
            },
        ]

ARTICLES = [
        {
            'name_de': 'Party Samstag Abend',
            'name_en': 'Party Saturday Evening',

            'price': 20,
            'no_articles_initially': 80,
            },
        {
            'name_de': 'Schlafen im Dojo',
            'name_en': 'Sleeping in the Dojo',

            'price': 0,
            'no_articles_initially': 30,
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
