from dataclasses import dataclass
from environs import Env


@dataclass
class Bot:

    token: str
    admin_id: str
    app_url: str


@dataclass
class Config:

    bot: Bot


def load_config(path: str | None) -> Config:

    env = Env()
    env.read_env(path)

    return Config(
        bot=Bot(
            token=env('BOT_TOKEN'),
            admin_id=env('ADMIN_ID'),
            app_url=('APP_URL')
        )
    )


x = 10
