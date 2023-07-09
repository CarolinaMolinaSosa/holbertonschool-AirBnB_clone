#!/usr/bin/python3
"""Tests for Place class"""


import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_place(self):
        place = Place()
        self.assertEqual(place.name, "")

    def test_type(self):
        city = Place()
        self.assertEqual(type(city.name), str)
        self.assertEqual(type(city.user_id), str)
        self.assertEqual(type(city.city_id), str)
        self.assertEqual(type(city.number_rooms), int)
        self.assertEqual(type(city.number_bathrooms), int)
        self.assertEqual(type(city.max_guest), int)
        self.assertEqual(type(city.price_by_night), int)
        self.assertEqual(type(city.latitude), float)
        self.assertEqual(type(city.longitude), float)
        self.assertEqual(type(city.amenity_ids), list)
        self.assertEqual(type(city.description), str)

    def test_public_attribute(self):
        city = Place()
        city.name = "Molly"
        city.user_id = "98765"
        city.city_id = "10"
        city.description = "Ok"
        city.number_rooms = 2
        city.number_bathrooms = 2
        city.max_guest = 1
        city.price_by_night = 500
        city.latitude = 1.3
        city.longitude = 1.1
        city.amenity_ids = ["10", "10"]
        self.assertEqual(city.name, "Molly")
        self.assertEqual(city.user_id, "98765")
        self.assertEqual(city.city_id, "10")
        self.assertEqual(city.description, "Ok")
        self.assertEqual(city.number_rooms, 2)
        self.assertEqual(city.number_bathrooms, 2)
        self.assertEqual(city.max_guest, 1)
        self.assertEqual(city.price_by_night, 500)
        self.assertEqual(city.latitude, 1.3)
        self.assertEqual(city.longitude, 1.1)
        self.assertEqual(city.amenity_ids, ["10", "10"])

    def test_instance(self):
        city = Place()
        self.assertIsInstance(city, type(Place()))

    def test_same_obj(self):
        citya = Place()
        cityb = Place()
        self.assertIsNot(citya, cityb)
