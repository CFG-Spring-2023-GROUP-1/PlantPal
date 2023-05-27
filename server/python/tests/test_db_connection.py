from unittest import TestCase
import sys
sys.path.append('../')
from connect_to_db import DBConnectionError, conn_exists


class TestDBConnection(TestCase):
    def test_custom_error_message(self):
        try:
            raise DBConnectionError('Test error')
        except DBConnectionError as e:
            assert str(e) == 'Test error'

    def test_conn_exists(self):
        self.assertEqual(conn_exists(), True)

    def test_conn_does_not_exists(self):
        self.assertEqual(not conn_exists(), False)

    

        