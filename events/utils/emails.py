
from events.models import Purchase
from associates.models import Associate

from django.core.mail import EmailMessage

from ikedaseminar import EMAIL_TEMPLATES


def send_confirmation_mail_for_purchase(purchase_pk):
    pur_obj = Purchase.objects.get(pk=purchase_pk)
    mail_body = create_confirmation_mail_body_for_purchase(pur_obj)

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


def create_confirmation_mail_body_for_purchase(pur_obj):
    ''' '''
    if pur_obj.associate.language == Associate.LANGUAGE_GERMAN:
        mail_body = EMAIL_TEMPLATES.REGISTRATION_EMAIL_DE.format(
                first_name='{fn}'.format(
                    fn=pur_obj.associate.first_name.encode('utf-8')),
                pid=pur_obj.pid,
                package=pur_obj.pretty_print(language='de'),
                associate=pur_obj.associate.pretty_print_basic(),
                message='{m}'.format(m=pur_obj.associate_message.encode('utf-8')),
                )
    else:
        mail_body = EMAIL_TEMPLATES.REGISTRATION_EMAIL_EN.format(
                first_name='{fn}'.format(
                    fn=pur_obj.associate.first_name.encode('utf-8')),
                pid=pur_obj.pid,
                package=pur_obj.pretty_print(language='en'),
                associate=pur_obj.associate.pretty_print_basic(),
                message='{m}'.format(m=pur_obj.associate_message.encode('utf-8')),
                )
    return mail_body

