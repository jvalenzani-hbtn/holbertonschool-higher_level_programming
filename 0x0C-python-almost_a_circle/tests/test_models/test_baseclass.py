#!/usr/bin/python3

from models.base import Base
import unittest

class TestBaseClass(unittest.TestCase):

    def test_instance_autonumber(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id - 1, b1.id)

    def test_new_instance(self):
        b = Base()
        self.assertTrue(isinstance(b, Base))

    def test_new_instance_id(self):
        id = 21
        b = Base(id)
        self.assertEqual(b.id, id)
    
    def test_not_num_id(self):
        id = "NaN"
        num = Base.nb_objects()
        b = Base(id)
        self.assertEqual(b.id, num+1)

if __name__ == '__main__':
    unittest.main()