from os import environ

from celery import Celery


def get_base_celery_app(module_name="tasks"):
    if (
        "BROKER_USER" not in environ
        or not environ["BROKER_USER"]
        or "BROKER_PASSWORD" not in environ
        or not environ["BROKER_PASSWORD"]
        or "BROKER_ENDPOINT" not in environ
        or not environ["BROKER_ENDPOINT"]
    ):
        raise Exception(
            "BROKER_USER, BROKER_PASSWORD and BROKER_ENDPOINT environment variables are required."
        )

    BROKER_USER = environ["BROKER_USER"]
    BROKER_PASSWORD = environ["BROKER_PASSWORD"]
    BROKER_ENDPOINT = environ["BROKER_ENDPOINT"]

    app = Celery(
        module_name,
        broker=f"amqps://{BROKER_USER}:{BROKER_PASSWORD}@{BROKER_ENDPOINT}:5671",
        backend="rpc://",
    )

    return app
