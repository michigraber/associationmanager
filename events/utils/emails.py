
from events.models import Purchase
from associates.models import Associate

from django.core.mail import EmailMessage

from ikedaseminar import EMAIL_TEMPLATES


def send_confirmation_mail_for_purchase(purchase_pk):
    pur_obj = Purchase.objects.get(pk=purchase_pk)

    if pur_obj.associate.language == Associate.LANGUAGE_GERMAN:
        mail_body = EMAIL_TEMPLATES.REGISTRATION_EMAIL_DE.format(
                first_name=u'{fn}'.format(fn=pur_obj.associate.first_name),
                pid=pur_obj.pid,
                package=pur_obj.pretty_print(language='de'),
                associate=pur_obj.associate.pretty_print_basic(),
                message=u'{m}'.format(m=pur_obj.associate_message),
                )
    else:
        mail_body = EMAIL_TEMPLATES.REGISTRATION_EMAIL_EN.format(
                first_name=pur_obj.associate.first_name,
                pid=pur_obj.pid,
                package=pur_obj.pretty_print(language='en'),
                associate=pur_obj.associate.pretty_print_basic(),
                message=pur_obj.associate_message,
                )

    email = EmailMessage(
            '[Hiroshi Ikeda Shihan Seminar Zurich 2014]',
            mail_body,
            'ikedaseminar@aikikai-zuerich.ch',
#           ['michigraber@gmail.com', ]
            [pur_obj.associate.email_address, ],
            ['michigraber@aikikai-zuerich.ch', 
             'herbert.looser@bluewin.ch', ],
            )
    email.send(fail_silently=False)
