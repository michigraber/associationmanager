from django.shortcuts import render_to_response
from django.core.context_processors import csrf

from .models import Event 
from .forms import SelectPurchaseItemsForm


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
                'form': SelectPurchaseItemsForm(event=event, language=lang),
                }
    context.update(csrf(request))
    return render_to_response('registration.html', context) 
