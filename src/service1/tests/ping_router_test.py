import unittest
from service1.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


class PingRouterTestCase(unittest.TestCase):
    def test_ping_response_code(self):
        response = client.get("/ping")
        self.assertEqual(response.status_code, 200)
