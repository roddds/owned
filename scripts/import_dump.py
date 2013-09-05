#! -*- coding: utf-8 -*-

import json
import sys
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
         26: u'DUMMY',
         27: u'DUMMY',
         28: u'Mochila',
         29: u'Kit de Primeiros Socorros',
         30: u'Óculos de Sol Modelo Audrey Hepburn'}

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


    print "creating events..."
    for key, label in EVENTS.iteritems():
        i = Event.objects.create(label=label)
        i.save()


    print "parsing paragraphs..."
    paragraphs = []
    for item in sorted([int(x) for x in jsonfile.keys()]):
        paragraphs.append(jsonfile[str(item)])


    print "creating paragraph objects..."
    for item in paragraphs:
        paragraph = Paragraph.objects.create(
            title=item['title'],
            text=item['text'])

        paragraph.save()

        if "Iniciar novo jogo" in item['option1']:
            paragraph.is_ending = True
            print "found ending in paragraph #%d" % paragraph.pk
            paragraph.save()

        print "creating game options for chapter %d..." % paragraph.pk
        for i in range(1, 6):
            if item.get('option%d' % i):
                op = Option.objects.create(
                    text = item['option%d' % i],
                    target = item['target%d' % i]
                    )
                op.save()

                if item.get('flags%d' % i):
                    option_flags = parse_flags(item['flags%d' % i])
                    for flag in option_flags:
                        pk, status = flag
                        req = Item.objects.get(pk=pk)
                        req.has = False if status=='0' else True
                        req.save()
                        op.item_requirements.add(req)

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
                req.has = False if status=='0' else True
                req.save()
                paragraph.adds_events.add(req)

        if item.get('itens'):
            print "adding flag setters"
            items = parse_flags(item['itens'])
            for flag in items:
                pk, status = flag
                req = Item.objects.get(pk=pk)
                req.has = False if status=='0' else True
                req.save()
                paragraph.adds_items.add(req)



    

    print "finished!"