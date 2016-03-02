# -*- coding: utf8 -*-
from django.test import TestCase
from model_mommy import mommy


class TestChapterOption(TestCase):

    def setUp(self):
        self.option = mommy.make('book.Option')
        self.slot = mommy.make('users.SaveSlot')

    def tearDown(self):
        self.option.delete()
        self.slot.delete()

    def test_option_no_requirements(self):
        "testa opção sem exigências"
        self.assertTrue(self.option.requirements_met(self.slot))

    def test_option_item_requirement_not_met(self):
        "testa opção com exigência de item não atendida"
        self.option.required_items.add(mommy.make('book.Item'))

        self.assertFalse(self.option.requirements_met(self.slot))

    def test_option_event_requirement_not_met(self):
        "testa opção com exigência de evento não atendida"
        self.option.required_events.add(mommy.make('book.Event'))

        self.assertFalse(self.option.requirements_met(self.slot))

    def test_option_item_requirement_met(self):
        "testa opção com exigência de item atendida"
        item = mommy.make('book.Item')
        self.option.required_items.add(item)
        self.slot.inventory.add(item)

        self.assertTrue(self.option.requirements_met(self.slot))

    def test_option_event_requirement_met(self):
        "testa opção com exigência de evento atendida"
        event = mommy.make('book.Event')

        self.option.required_events.add(event)
        self.slot.events.add(event)

        self.assertTrue(self.option.requirements_met(self.slot))

    def test_option_event_met_item_not_met(self):
        "testa opção com exigência de evento atendida mas de item não"
        event = mommy.make('book.Event')
        item = mommy.make('book.Item')

        self.option.required_events.add(event)
        self.slot.events.add(event)

        self.option.required_items.add(item)

        self.assertFalse(self.option.requirements_met(self.slot))

    def test_option_item_met_event_not_met(self):
        "testa opção com exigência de item atendida mas de evento não"
        event = mommy.make('book.Event')
        item = mommy.make('book.Item')

        self.option.required_items.add(item)
        self.slot.inventory.add(item)

        self.option.required_events.add(event)

        self.assertFalse(self.option.requirements_met(self.slot))

    ## exclusion

    def test_option_item_exclusion_not_met(self):
        "testa opção com exclusão de item não atendida"
        self.option.excluding_items.add(mommy.make('book.Item'))

        self.assertTrue(self.option.requirements_met(self.slot))

    def test_option_event_exclusion_not_met(self):
        "testa opção com exclusão de evento não atendida"
        event = mommy.make('book.Event')
        self.option.excluding_events.add(event)
        self.slot.events.add(event)

        self.assertFalse(self.option.requirements_met(self.slot))

    def test_option_item_exclusion_met(self):
        "testa opção com exclusão de item atendida"
        item = mommy.make('book.Item')
        self.option.excluding_items.add(item)
        self.slot.inventory.add(item)

        self.assertFalse(self.option.requirements_met(self.slot))

    def test_option_event_exclusion_met(self):
        "testa opção com exclusão de evento atendida"
        event = mommy.make('book.Event')

        self.option.excluding_events.add(event)
        self.slot.events.add(event)

        self.assertFalse(self.option.requirements_met(self.slot))

    def test_option_event_exclusion_item_not(self):
        "testa opção com exclusão de evento atendida mas de item não"
        event = mommy.make('book.Event')
        item = mommy.make('book.Item')

        self.option.excluding_events.add(event)
        self.slot.events.add(event)

        self.option.excluding_items.add(item)

        self.assertFalse(self.option.requirements_met(self.slot))

    def test_option_item_exclusion_event_not(self):
        "testa opção com exclusão de item atendida mas de evento não"
        event = mommy.make('book.Event')
        item = mommy.make('book.Item')

        self.option.excluding_items.add(item)
        self.slot.inventory.add(item)

        self.option.excluding_events.add(event)

        self.assertFalse(self.option.requirements_met(self.slot))

