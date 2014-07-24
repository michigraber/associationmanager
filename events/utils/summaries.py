
from .. import models

def associates_for_event(event, display=True):
    ''' '''
    if type(event) == int:
        event = models.Event.objects.get(pk=1)
    
    ep_associates = {}
    for ep in event.eventpart_set.all():
        epname = ep.short_description_en
        ep_associates[epname] = []
        for registration in ep.registration_set.all():
            if registration.associate not in ep_associates[epname]:
                if registration.is_paid_or_pending():
                    ep_associates[epname].append(registration.associate)
        ep_associates[epname] = sorted(list(set(ep_associates[epname])))

    if display:
        print '\n'+50*'* '+'\n', event.title_en, '\n'+50*'* '+'\n'

        for ep in ep_associates:
            print '\n', ep, ' : ', len(ep_associates[ep]), ' Registrations\n'+50*'--'+'\n'
            for ass in ep_associates[ep]:
                print u'o   {ln} {fn}, {city}, {country}\n'.format(
                        ln=ass.last_name, fn=ass.first_name,
                        city=ass.city, country=ass.country)

        associate_set = []
        for ep in ep_associates:
            associate_set.extend(ep_associates[ep])
        associate_set = sorted(list(set(associate_set)))

    return associate_set
