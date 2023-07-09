#!/usr/bin/python3
"""Tests for City class"""


import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def test_city(self):
        city = City()
        self.assertEqual(city.name, "")

    def test_type(self):
        city = City()
        self.assertEqual(type(city.name), str)
        self.assertEqual(type(city.state_id), str)

    def test_public_attribute(self):
        city = City()
        city.name = "Molly"
        city.state_id = "98765"
        self.assertEqual(city.name, "Molly")
        self.assertEqual(city.state_id, "98765")

    def test_instance(self):
        city = City()
        self.assertIsInstance(city, type(City()))

    def test_same_obj(self):
        citya= City()
        cityb = City()
        self.assertIsNot(citya, cityb)
