# coding: utf-8
import requests
import re
import environ

env = environ.Env()

PAGE_ACCESS_TOKEN = env('DJANGO_EMAIL_BACKEND')


def call_send_api(message_data):
    response = requests.post(
        url='https://graph.facebook.com/v2.6/me/messages',
        params={'access_token': PAGE_ACCESS_TOKEN},
        json=message_data,
    )

    if response.status_code == 200:
        recipient_id = response.json()['recipient_id']
        message_id = response.json()['message_id']

        print 'Successfully sent message with id %s to recipient %s' % (recipient_id, message_id)
    else:
        print 'Failed calling Send API', response.status_code, response.json()['error'], '\n', message_data


def send_text_message(recipient_id, message_text):
    message_data = {
        'recipient': {
            'id': recipient_id
        },
        'message': {
            'text': message_text,
            'metadata': 'DEVELOPER_DEFINED_METADATA'
        }
    }

    call_send_api(message_data);


def get_option_text(option):

    if option.target == 1 and option.text.startswith('Iniciar novo jogo'):
        return 'New game'
    elif option.text.lower().startswith('se'):
        return u'Vá para %s' % option.target
    elif option.text.lower().startswith(u'vá para'):
        return 'Continuar...'

    special_cases = {
        10:  u'Entrar no 410',
        114: u'Não copia nada',
        119: u'Acredita em Rosana',
        124: u'Convence a escrever',
        125: u'Não vale a pena',
        130: u'Dafne',
        134: u'Acredita em Samara',
        141: u'Nenhuma das duas',
        151: u'Voltar',
        193: u'Ler o livro dela',
        1:   u'Tente de novo',
        205: u'Elza',
        212: u'GANHA MEU PODER',
        215: u'Isso é você?',
        232: u'Faz cópia também',
        255: u'Faz o planejado',
        265: u'Isso é você?',
        30:  u'Eu não li NADA!',
        38:  u'GANHA NA MEGASENA',
        65:  u'Voltar',
        91:  u'Tá, eu li o walkthru',
    }

    if option.target in special_cases.keys():
        return special_cases[option.target]

    text = option.text

    text = text.split(u'– vá para')[0]
    text = text.split(u' – ')[0]
    text = text.split(u', vá para')[0]
    text = text.replace('.', '').strip()
    text = text.replace(u'– ', '').strip()
    text = re.sub('\(.*?\)', '', text)

    if text.startswith(u'Você'):
        text = text.replace(u'Você', '')

    text = text.strip().capitalize()

    return text


def send_options(recipient_id, slot, paragraph):

    paragraph_options = paragraph.options.all()
    valid_options = [
        option for option
        in paragraph_options
        if option.requirements_met(slot)
    ]

    buttons = [{
        'type': 'postback',
        'title': get_option_text(option),
        'payload': option.target,
        } for option in valid_options
        if option.target not in (207, 257)
    ]

    if len(buttons) == 1:
        title = 'Clique para continuar'
    else:
        title = u'Qual é a sua escolha?'

    message_data = {
        'recipient': {
            'id': recipient_id
        },
        'message': {
            'attachment': {
                'type': 'template',
                'payload': {
                    'template_type': 'button',
                    'text': title,
                    'buttons': buttons
                }
            }
        }
    }

    call_send_api(message_data)
