import unittest
from pyrest import PyRest, PendingCall

class TestPyRest(unittest.TestCase):

    def test_base(self):
        #http://api.openweathermap.org/data/2.5/weather?q=London,uk
        data = PyRest('http://api.openweathermap.org').data["2.5"].weather.get(q="London,uk")
        self.assertEqual(data["name"], "London")

    def test_subclass(self):
        class SubRest(PyRest):
            def __init__(self, url, username, password):
                super().__init__(url)
                self.username = username
                self.password = password

            def create_pending_call(self):
                return PendingCall(
                  self.url,
                  username=self.username,
                  password="__{}".format(self.password),
                )

        call = SubRest("http://test.com", "john", "pass").model.view["1"]
        self.assertEqual(call.url, "http://test.com/model/view/1")
        self.assertEqual(call.params, {"username": "john", "password": "__pass"})



if __name__ == '__main__':
    unittest.main()
