from apiclient import APIClient, endpoint

from decouple import config

BASE_URL = config("http://10.100.9.81:31936/api/v1")


@endpoint(base_url=BASE_URL)
class Endpoint:
    login = "auth/login"


class TeleagronomClient(APIClient):
    def login(self):
        return self.post(Endpoint.login, params)
