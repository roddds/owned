# coding: utf-8
import time
import re
from pprint import pprint

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import StreamingHttpResponse
from django.utils.html import strip_tags

from owned.users.models import User
from owned.book.models import Paragraph
from owned.chatbot.api import (
    send_text_message,
    send_options,
)

def split_paragraph(paragraph):
    string = strip_tags(paragraph)
    string = string.replace('\r', '')

    lines = []

    for line in re.findall('^.*', string, re.MULTILINE):
        line = line.strip()

        if not line:
            continue

        elif len(line) < 640:
            lines.append(line)

        else:
            phrases = re.findall('[^.]*[^.]*\.', line)
            newline = ''

            while phrases:
                phrase = phrases.pop()

                if len(newline) + len(phrase) < 640:
                    newline += phrase
                else:
                    lines.append(newline)
                    newline = ''

            if newline:
                lines.append(newline)

    return lines


def new_game(user):
    user.setup()
    slot = user.save_slots.get_slot(1)
    slot.set_as_active()
    slot.new_game()

    return slot

def send_current_chapter(sender, slot):
    paragraph = Paragraph.objects.get(id=slot.current_chapter)

    for line in split_paragraph(paragraph.text):
        send_text_message(sender, line)

    send_options(sender, slot, paragraph)


def process_turn(message):
    sender = message['sender']['id']

    user, created = User.objects.get_or_create(username=sender)

    if created:
        print 'created new user'
        slot = new_game(user)
    else:
        slot = user.active_save_slot

    if message.get('postback'):
        chapter = message['postback']['payload']
        slot.play_chapter(chapter)
        send_current_chapter(sender, slot)

    elif message.get('message'):
        message = message['message']['text']
        if message.lower() == 'new game':
            slot = new_game(user)

            send_current_chapter(sender, slot)


class Home(APIView):
    def post(self, request):
        pprint(request.data)

        for entries in request.data['entry']:
            for message in entries['messaging']:
                process_turn(message)

        return StreamingHttpResponse('ok')
