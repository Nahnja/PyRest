import requests

class PendingCall():

    def __init__(self, url, **params):
        self.url = url.rstrip("/")
        self.params = params

    def __getattr__(self, attr):
        return self[attr]

    def __getitem__(self, key):
        self.url = self.url + "/" + str(key)
        return self

    def __repr__(self):
        return "PendingCall('{}', **{})".format(str(self.url), str(self.params))

    def get(self, **params):
        self.params.update(params)
        return requests.get(self.url, params=self.params).json()

    def post(self, **params):
        self.params.update(params)
        return requests.post(self.url, data=self.params).json()

    def put(self, **params):
        self.params.update(params)
        return requests.put(self.url, data=self.params).json()

    def delete(self, **params):
        self.params.update(params)
        return requests.delete(self.url, params=self.params).json()


class PyRest():

    def __init__(self, url):
        self.url = url

    def create_pending_call(self):
        return PendingCall(self.url)

    def __getattr__(self, attr):
        return self[attr]

    def __getitem__(self, key):
        return self.create_pending_call()[key]


# http://api.openweathermap.org/data/2.5/weather?q=London,uk
