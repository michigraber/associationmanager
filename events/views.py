
from django.shortcuts import render_to_response
from django.contrib.formtools.wizard.views import SessionWizardView

from django.core.context_processors import csrf

from associates.forms import AssociateForm_de

from .models import Event 
from .forms import SelectPurchaseItemsForm, RegistrationMessage


class RegistrationWizard(SessionWizardView):

    form_list = [SelectPurchaseItemsForm, AssociateForm_de,
            RegistrationMessage]
#   form_list = [AssociateForm_de, RegistrationMessage]

    template_name = 'registration.html'

    def get_context_data(self, form, **kwargs):
        context = super(SessionWizardView, self).get_context_data(form=form,
                **kwargs)
        context.update(self.kwargs)
        return context

    def get_form_kwargs(self, step):
        # this was apparently wrong, ay?
        return self.initial_dict[step]
    
    def done(self, form_list, **kwargs):
        # do something with the form data
        return render_to_response('checkout.html', {
            'form_data': [form.cleaned_data for form in form_list],
            'language': self.kwargs['language'],
        })


def select_purchase_items(request, lang=''):
    event = Event.objects.get(pk=1)
    if request.method == 'POST':
        form = SelectPurchaseItemsForm(request.POST, event=event,
                language=lang)
        selection_summary = []
        if form.is_valid():
            for fk, fv in form.fields.iteritems():
                selection_summary.append(fk)
        context = {
                'request_method': request.method,
                'registration_step' : 2,
                'language': lang,
                'selection_summary': selection_summary, 
                'form': form,
                }
        context.update(csrf(request))
        return render_to_response('registration.html', context)
    else:
        event = Event.objects.get(pk=1)
        context = { 
                'request_method': request.method,
                'registration_step' : 1,
                'language': lang,
                'form': RegistrationMessage(),
                #'form': SelectPurchaseItemsForm(event=event, language=lang),
                }
    context.update(csrf(request))
    return render_to_response('registration.html', context) 
