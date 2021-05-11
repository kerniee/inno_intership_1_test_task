from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import StateFilter


class MyStateFilter(StateFilter):
    api_client = None

    def __init__(self, dispatcher, state):
        super().__init__(dispatcher, state)

    @staticmethod
    async def set_auth_token(state: FSMContext):
        async with state.proxy() as data:
            try:
                MyStateFilter.api_client.configuration.api_key = {"Authorization": data["token"]}
            except KeyError:
                return

    async def check(self, obj):
        await MyStateFilter.set_auth_token(self.dispatcher.current_state())
        return await super().check(obj)
