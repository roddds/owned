#! -*- coding: utf-8 -*-
import os
import json
import sys
import re
from django.contrib.auth.models import User
from player.models import Player, SaveSlot
from book.models import Option, Paragraph, Event, Item
from itertools import izip


def parse_flags(flags):
    f = flags.split('{')[1][:-1]
    f = iter(f.split(";"))
    f = ["-".join(x) for x in izip(f, f)]
    return [x.replace("i:", "").split("-") for x in f]

ITEMS = {1:  u'Amuleto',
         2:  u'Chave-Mestra',
         3:  u'Cópia do HD de Laila',
         4:  u'E-Mail de Confirmação',
         5:  u'iPod de Mayumi',
         6:  u'Moedeira',
         7:  u'Nota de Cem Reais',
         8:  u'Tupperware da Mayumi',
         9:  u'Panfleto',
         10: u'Moedeira (cheia)',
         11: u'Console Vintage Original',
         12: u'Coxinha',
         13: u'HD Externo do Edgar',
         14: u'Prejuízo de 10%',
         15: u'Submetralhadora',
         16: u'Munição de Submetralhadora',
         17: u'Pistola',
         18: u'Saquinho (Patuá)',
         19: u'Maleta 007',
         20: u'Chave de Saída',
         21: u'Chave de Fenda',
         22: u'Vassoura',
         23: u'Chave Comum',
         24: u'Fuzil',
         25: u'Granadas',
         28: u'Mochila',
         29: u'Kit de Primeiros Socorros',
         30: u'Óculos de Sol Modelo Audrey Hepburn'}


ITEM_IMAGES = {u"Amuleto":                             'amuleto.png',
               u"Chave-Mestra":                        'chave_mestra.png',
               u"Cópia do HD de Laila":                'copia_hd_laila.png',
               u"E-Mail de Confirmação":               'email.png',
               u"iPod de Mayumi":                      'ipod.png',
               u"Moedeira":                            'moedeira.png',
               u"Nota de Cem Reais":                   'nota_de_100.png',
               u"Tupperware da Mayumi":                'tupperware.png',
               u"Panfleto":                            'panfleto.png',
               u"Moedeira (cheia)":                    'moedeira_cheia.png',
               u"Console Vintage Original":            'console_vintage.png',
               u"Coxinha":                             'coxinha.png',
               u"HD Externo do Edgar":                 'hd_do_edgar.png',
               u"Prejuízo de 10%":                     'prejuizo.png',
               u"Submetralhadora":                     'submetralhadora.png',
               u"Munição de Submetralhadora":          'municao.png',
               u"Pistola":                             'pistola.png',
               u"Saquinho (Patuá)":                    'saquinho.png',
               u"Maleta 007":                          'maleta_007.png',
               u"Chave de Saída":                      'chave_de_saida.png',
               u"Chave de Fenda":                      'chave_de_fenda.png',
               u"Vassoura":                            'vassoura.png',
               u"Chave Comum":                         'chave_comum.png',
               u"Fuzil":                               'fuzil.png',
               u"Granadas":                            'granada.png',
               u"Mochila":                             'mochila.png',
               u"Kit de Primeiros Socorros":           'kit_primeiros_socorros.png',
               u"Óculos de Sol Modelo Audrey Hepburn": 'oculos.png'}

EVENTS = {1:  u"Esteve num acampamento",
          2:  u"Jantou na casa de alguém",
          3:  u"Foi ao cinema",
          4:  u"Aceitou o Amuleto",
          5:  u"Ficou no carro de Fernando na favela",
          6:  u"Foi atrás de Fernando na favela",
          7:  u"Tem falado sobre um livro com alguém no chat",
          8:  u"Falou com DAFNE",
          9:  u"Entrou num quarto usando uma chave-mestra",
          10: u"Esteve numa boate",
          11: u"Falou com ELZA",
          12: u"Disse a Samara: “você está confusa” - no 171 ou 263",
          13: u"Disse a Samara que NÃO tiraria os poderes de Laila se pudesse",
          14: u"Disse a Samara que tiraria os poderes de Laila se pudesse",
          15: u"Dassou por um temporal",
          16: u"Entrou num quarto fechado usando uma chave-mestra",
          17: u"Deu o Amuleto a alguém (Rosana)"}

def run():
    print "reading json file..."
    with open("dump.json") as f:
        jsonfile = json.load(f)

    print "creating items..."
    for key, name in ITEMS.iteritems():
        i = Item.objects.create(name=name)
        i.save()
        print "\tcreated item %s" % i.name

    print "creating events..."
    for key, label in EVENTS.iteritems():
        i = Event.objects.create(label=label)
        i.save()
        print "\tcreated event %s" % label

    print "parsing paragraphs..."
    paragraphs = []
    for item in sorted([int(x) for x in jsonfile.keys()]):
        paragraphs.append(jsonfile[str(item)])

    print "creating paragraph objects..."
    for item in paragraphs:
        text = item['text']
        text = '\n'.join([x.strip() for x in text.split('\n')])
        text = text.replace("<br />", "</p>\n<p>")
        text = text.replace("<p>\n", "<p>")
        if re.findall('<a.+">', text):
            text = text.replace(re.findall('<a.+">', text)[0], '')
        text = text.replace("</a>", "")

        paragraph = Paragraph.objects.create(
                title = item['title'],
                text  = text)
        paragraph.save()
        print "created paragraph #%d" % paragraph.pk

        if "Iniciar novo jogo" in item['option1']:
            paragraph.is_ending = True
            print "found ending in paragraph #%d" % paragraph.pk
            paragraph.save()

        print "creating game options for chapter %d..." % paragraph.pk
        for i in range(1, 6):
            if item.get('option%d' % i):
                op = Option.objects.create(
                    text   = item['option%d' % i],
                    target = item['target%d' % i])
                op.save()
                print "created option %d" % op.pk

                print "setting option flags for option %d" % op.pk
                if item.get('flags%d' % i):
                    option_flags = parse_flags(item['flags%d' % i])
                    for flag in option_flags:
                        pk, status = flag
                        req = Event.objects.get(pk=pk)
                        if status == "1":
                            op.required_events.add(req)
                            print "added event requirement of having %s to option %d on paragraph %d" % (req.label, i, paragraph.pk)
                        else:
                            op.excluding_events.add(req)
                            print "added item requirement of not having %s to option %d on paragraph %d" % (req.label, i, paragraph.pk)
                        op.save()

                if item.get('itens%d' % i):
                    option_flags = parse_flags(item['itens%d' % i])
                    for flag in option_flags:
                        pk, status = flag
                        req = Item.objects.get(pk=pk)
                        if status == "1":
                            op.required_items.add(req)
                            print "added item requirement of having %s to option %d on paragraph %d" % (req.name, i, paragraph.pk)
                        else:
                            op.excluding_items.add(req)
                            print "added item requirement of not having %s to option %d on paragraph %d" % (req.name, i, paragraph.pk)
                        op.save()

                op.paragraph = paragraph
                op.save()

        if item.get('flags'):
            print "adding flag setters"
            flags = parse_flags(item['flags'])
            for flag in flags:
                pk, status = flag
                if int(pk) >= 18:
                    break
                req = Event.objects.get(pk=pk)
                # req.has = False if status=='0' else True
                # req.save()
                if status != "0":
                    paragraph.adds_events.add(req)
                    print "paragraph %d adds event %s" % (paragraph.pk,
                                                          req.label)

        if item.get('itens'):
            print "adding item setters"
            items = parse_flags(item['itens'])
            for flag in items:
                pk, status = flag
                req = Item.objects.get(pk=pk)
                # req.has = False if status=='0' else True
                # req.save()
                if status != "0":
                    paragraph.adds_items.add(req)
                    print "paragraph %d adds item %s" % (paragraph.pk,
                                                         req.name)
                else:
                    paragraph.removes_items.add(req)
                    print "paragraph %d removes item %s" % (paragraph.pk,
                                                            req.name)

    print "restoring custom paragraphs"
    files = os.listdir("scripts/chapters/")
    for i in files:
        with open(os.path.join("scripts/chapters/", i)) as f:
            text = f.read()
            p = Paragraph.objects.get(pk=i.split(".")[0])
            p.text = text
            p.save()
            print "restored %s" % i

    print "fixing logic from previous code"
    p = Paragraph.objects.get(pk=1)
    p.adds_items.clear()
    p.removes_items.clear()
    p.adds_events.clear()
    p.save()

    print "adding item image filenames"
    for name, filename in ITEM_IMAGES.iteritems():
        item = Item.objects.get(name=name)
        item.image_filename = filename
        item.save()

    print "finished!"
