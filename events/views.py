
from django.shortcuts import render_to_response
from django.contrib.formtools.wizard.views import SessionWizardView

from django.core.context_processors import csrf

from associates.forms import AssociateForm_de, EmergencyContactForm_de,\
        AssociateForm_en, EmergencyContactForm_en
from associates.models import Associate

from events.models import Event, EventPart, Registration, Purchase



from .forms import SelectPurchaseItemsForm, RegistrationMessageForm_de,\
        RegistrationMessageForm_en


EVENTPART_SET_PRICE_MAPPING = {
        0 : 0., 
        1 : 30.,
        2 : 60.,
        3 : 80.,
        4 : 100., 
        5 : 120.
        }


def registration_configuration(request, language=''):
    event = Event.objects.get(pk=1)
    
    # POST : Forms are filled in
    if request.method == 'POST':
        sel_form = SelectPurchaseItemsForm(request.POST, event=event, language=language)
        if language == 'de':
            ass_form = AssociateForm_de(request.POST)
            em_form = EmergencyContactForm_de(request.POST)
            mess_form = RegistrationMessageForm_de(request.POST)
        elif language == 'en':
            ass_form = AssociateForm_en(request.POST)
            em_form = EmergencyContactForm_en(request.POST)
            mess_form = RegistrationMessageForm_en(request.POST)
        else:
            raise ValueError('language has to be from ("de", "en")')

        if ass_form.is_valid() and em_form.is_valid() and mess_form.is_valid()\
                and sel_form.is_valid():
            print sel_form.cleaned_data
            
            # find Associate
            ass, created = Associate.objects.get_or_create(
                    email_address=ass_form.cleaned_data['email_address'],
                    date_of_birth=ass_form.cleaned_data['date_of_birth'],
                    )
            for fk, fv in ass_form.cleaned_data.iteritems():
                setattr(ass, fk, fv)
            for fk, fv in em_form.cleaned_data.iteritems():
                setattr(ass, fk, fv)

            # find EventParts
            eps = []
            arts = []
            for fk, fv in sel_form.cleaned_data.iteritems():
                if fv:
                    if language == 'de':
                        ep = event.eventpart_set.filter(short_description_de=fk)
                        try:
                            art = event.article_set.filter(name_de=fk)
                        except:
                            art = None
                    elif language == 'en':
                        ep = event.eventpart_set.filter(short_description_en=fk)
                        try:
                            art = event.article_set.get(name_de=fk)
                        except:
                            art = None
                    if ep:
                        eps.append(ep)
                    elif art:
                        arts.append(art)

            print 
            print eps
            print arts
            print
                
            # FIXME : this price calculation is not general!!
            price = int(EVENTPART_SET_PRICE_MAPPING[len(eps)] + len(arts)*10.)
            paypal_item_id = str(len(eps))+'K'+len(arts)*'P'


            context = {
                    'language': language,
                    'registration_step': 2,
                    'associate': ass,
                    'eventparts': eps,
                    'articles': arts,
                    'price': price,
                    'paypal_item_id': paypal_item_id,
                    }

            return render_to_response('registration.html', context)

    
    # GET : ENTRY POINT 
    else:
        sel_form = SelectPurchaseItemsForm(event=event, language=language)
        if language == 'de':
            ass_form = AssociateForm_de()
            em_form = EmergencyContactForm_de()
            mess_form = RegistrationMessageForm_de()
        elif language == 'en':
            ass_form = AssociateForm_en()
            em_form = EmergencyContactForm_en()
            mess_form = RegistrationMessageForm_en()
        else:
            raise ValueError('language has to be from ("de", "en")')
    
    context = { 
            'language': language,
            'registration_step' : 1,
            'event': event,
            'selection_form': sel_form,
            'associate_form': ass_form,
            'emergencycontact_form': em_form,
            'message_form': mess_form, 
            }

    context.update(csrf(request))
    return render_to_response('registration.html', context) 


def registration_paypal_return(request, language=None, status=None):

    print 
    print 'PAYPAL RETURN !!!!'
    method  = request.method
    if request.method == 'POST':
        post = request.POST
    else:
        None


    context = {
            'language': language,
            'status': status, 
            'method': method,
            'POST', post,
            }
    return render_to_response('checkout.html', context) 
