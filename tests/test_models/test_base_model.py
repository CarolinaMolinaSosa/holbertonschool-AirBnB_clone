#!/usr/bin/python3
"""Tests for BaseModel class"""

import unittest
from models.base_model import BaseModel
import models
from datetime import datetime
from time import sleep
import os


class TestBaseModel(unittest.TestCase):

    def test_id(self):
        basem1 = BaseModel()
        basem2 = BaseModel()
        self.assertNotEqual(basem1.id, basem2.id)

    def test_dict(self):
        basem = BaseModel()
        basem_dictionary = basem.to_dict()
        self.assertEqual(isinstance(basem_dictionary, dict), True)
        self.assertEqual(str(type(basem_dictionary)), "<class 'dict'>")

    def test_save(self):
        upd = BaseModel()
        basem = upd.updated_at
        upd.save()
        a = upd.updated_at
        self.assertNotEqual(basem, a)

    def test_created_at(self):
        ca = BaseModel()
        basem = datetime.now()
        c = ca.created_at
        self.assertNotEqual(c, basem)


class Test_instantiation(unittest.TestCase):

    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_inst_stored(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_dtime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_upd_dtime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_created_at(self):
        basem = BaseModel()
        sleep(0.05)
        b1 = BaseModel()
        self.assertLess(basem.created_at, b1.created_at)

    def test_two_models_different_updated_at(self):
        basem = BaseModel()
        sleep(0.05)
        b1 = BaseModel()
        self.assertLess(basem.updated_at, b1.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        basem = BaseModel()
        basem.id = "123456"
        basem.created_at = basem.updated_at = dt
        bstr = basem.__str__()
        self.assertIn("[BaseModel] (123456)", bstr)
        self.assertIn("'id': '123456'", bstr)
        self.assertIn("'created_at': " + dt_repr, bstr)
        self.assertIn("'updated_at': " + dt_repr, bstr)

    def test_args_unused(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        basem = BaseModel(id="11111", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(basem.id, "11111")
        self.assertEqual(basem.created_at, dt)
        self.assertEqual(basem.updated_at, dt)
        self.assertEqual(basem.created_at, basem.updated_at)


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        basem = BaseModel()
        self.assertTrue(dict, type(basem.to_dict()))

    def test_to_dict_contains_all_keys(self):
        basem = BaseModel()
        basem.name = "Molly"
        basem.my_number = 20
        self.assertIn("id", basem.to_dict())
        self.assertIn("created_at", basem.to_dict())
        self.assertIn("updated_at", basem.to_dict())
        self.assertIn("__class__", basem.to_dict())
        self.assertIn("name", basem.to_dict())
        self.assertIn("my_number", basem.to_dict())

    def test_to_dict_contains_attributes(self):
        basem = BaseModel()
        basem.name = "Molly"
        basem.my_number = 20
        self.assertIn("name", basem.to_dict())
        self.assertIn("my_number", basem.to_dict())


if __name__ == "__main__":
    unittest.main()
