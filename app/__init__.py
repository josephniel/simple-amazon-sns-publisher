from flask import Flask

from app.client import client
from app.router import ROUTES
from app.utils import import_submodules


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('app.config.BaseConfig')
    app.config.from_envvar('ENVIRONMENT_CONFIG_FILE')

    client.init_app(app)

    import_submodules(__name__)
    app.url_map.strict_slashes = False
    for route in ROUTES:
        app.add_url_rule(
            "{location}".format(location=route.location),
            view_func=route.view_func,
        )

    return app
