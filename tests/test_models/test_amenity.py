#!/usr/bin/python3
"""Tests for Amenity class"""


import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_amenity(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_type(self):
        amenity = Amenity()
        self.assertEqual(type(amenity.name), str)

    def test_public_attribute(self):
        amenity = Amenity()
        amenity.name = "Molly"
        self.assertEqual(amenity.name, "Molly")

    def test_instance(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, type(Amenity()))

    def test_same_obj(self):
        amenityA = Amenity()
        amenityB = Amenity()
        self.assertIsNot(amenityA, amenityB)
