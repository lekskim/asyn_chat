from unittest import TestCase, main
import json
import sys
import os
from lesson_06.client import presence_msg, preparing_message
from lesson_06.variables import *

basedir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(basedir)



class TestClient(TestCase):
    def test_presence_msg(self):
        result = presence_msg()
        self.assertEqual(type(result), bytes)

        obj = json.loads(result.decode(ENCODING))
        self.assertEqual(type(obj), dict)
        self.assertEqual(type(obj.get('action')), str)
        self.assertEqual(type(obj.get('time')), float)

    def test_preparing_message(self):
        result = preparing_message(msg='Hello world', action='msg')
        self.assertEqual(type(result), bytes)

        obj = json.loads(result.decode(ENCODING))
        self.assertEqual(obj.get('message'), 'Hello world')
        self.assertEqual(type(obj.get('action')), str)
        self.assertEqual(obj.get('action'), 'msg')
        self.assertEqual(type(obj.get('time')), float)


if __name__ == '__main__':
    main()

