import unittest
import requests

# Requires the app to be running
class RunAppTestCase(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__()
        
    def runTest(self):
        response = requests.get("http://localhost:5000/api/test")
        json = response.json()
        self.assertTrue(json["success"])
        self.assertEqual(json["message"], "Server running!")
