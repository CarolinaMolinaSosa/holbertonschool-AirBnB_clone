#!/usr/bin/python3
"""Tests for State class"""


import unittest
from models.state import State


class TestState(unittest.TestCase):
    def test_state(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_type(self):
        state = State()
        self.assertEqual(type(state.name), str)

    def test_public_attribute(self):
        state = State()
        state.name = "Molly"
        self.assertEqual(state.name, "Molly")

    def test_instance(self):
        state = State()
        self.assertIsInstance(state, type(State()))

    def testi_same_object(self):
        statea = State()
        stateb = State()
        self.assertIsNot(statea, stateb)
