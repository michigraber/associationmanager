
from .. import models

def associates_for_event(event, display=True):
    ''' '''
    if type(event) == int:
        event = models.Event.objects.get(pk=event)
    
    ep_associates = {}
    for ep in event.eventpart_set.all():
        epname = ep.short_description_en
        ep_associates[epname] = ep.get_participants()

    for article in event.article_set.all():
        ep_associates[article.name_en] = article.get_buyers()

    if display:
        print '\n'+50*'* '+'\n', event.title_en, '\n'+50*'* '+'\n'

        for ep in ep_associates:
            print '\n', ep, ' : ', len(ep_associates[ep]), ' Registrations\n'+50*'--'+'\n'
            for assdict in ep_associates[ep]:
                ass = assdict['ass']
                ps = assdict['payment_status']
                ps = '! '+ps.upper()+' !' if ps == 'pending' else ps

                print u'o   {ln} {fn}, {city}, {country} : {payment_status}\n'.format(
                        ln=ass.last_name, fn=ass.first_name,
                        city=ass.city, country=ass.country, payment_status=ps)

    associate_set = []
    for ep in ep_associates.values():
        for assdict in ep:
            if assdict['ass'] not in associate_set:
                associate_set.append(assdict['ass'])
    associate_set = sorted(associate_set, key=lambda k:k.sort_string)

    if display:

        print
        print
        print '\n'+50*'* '+'\n', 'PARTICIPANTS DETAILS', '\n'+50*'* '+'\n'

        for ass in associate_set:
            print
            print ass.last_name.upper(), ass.first_name
            print ass.street_and_nr, ', ', ass.postal_code, ass.city
            print ass.email_address
            if ass.emergency_contact_last_name or ass.emergency_contact_first_name or ass.emergency_contact_phone_number:
                print 'emergency contact: ', ass.emergency_contact_last_name, ass.emergency_contact_first_name, ' (', ass.emergency_contact_relationship, ') ', ass.emergency_contact_phone_number

    

    return associate_set
