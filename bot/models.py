import cachetools.func
from aiogram import Dispatcher, Bot

import swagger_client
from swagger_client import ApiClient, AuthApi, TeleagronomUser


class Determinants:
    def __init__(self, bot: Bot, dp: Dispatcher, api_client: ApiClient):
        self.dp = dp
        self.bot = bot
        self.api_client = api_client
        self.determinant_api = swagger_client.V1determinantApi(api_client)

    @property
    @cachetools.func.ttl_cache(maxsize=1, ttl=60)
    def active(self):
        return self.determinant_api.determinant_active_retrieve()

    @property
    def names(self):
        active_determs = self.active
        return [s.name for s in active_determs]

    def id_from_name(self, name: str):
        active_determs = self.active
        for d in active_determs:
            if d.name.strip().lower() == name.strip().lower():
                return d.id


class Me:
    def __init__(self, bot: Bot, dp: Dispatcher, auth_api: AuthApi):
        self.dp = dp
        self.bot = bot
        self.auth_api = auth_api

    @property
    @cachetools.func.ttl_cache(maxsize=1, ttl=60)
    def me(self) -> TeleagronomUser:
        return self.auth_api.auth_users_me_retrieve()

    @property
    def id(self):
        return self.me.id
