from fastapi import FastAPI

from common.utils.singleton import Singleton


class AppGetter(Singleton):
    def __init__(self):
        self._app = FastAPI()

    def __call__(self) -> FastAPI:
        return self._app
