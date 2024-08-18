import uvicorn

from api.app import AppGetter
from common.config.config import Config


def main():
    config = Config.get_instance()
    uvicorn.run(AppGetter.get_instance()(), host=config.HOST, port=config.PORT)


if __name__ == "__main__":
    main()
