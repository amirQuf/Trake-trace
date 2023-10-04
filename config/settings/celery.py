from config.env import env
from datetime import timedelta
from trace.shipment.utils import WeatherAPICaller

# https://docs.celeryproject.org/en/stable/userguide/configuration.html

CELERY_BROKER_URL = env("CELERY_BROKER_URL", default="amqp://guest:guest@localhost//")
CELERY_RESULT_BACKEND = "django-db"

CELERY_TIMEZONE = "UTC"

CELERY_TASK_SOFT_TIME_LIMIT = 20  # seconds
CELERT_TASK_TIME_LIMIT = 30  # seconds
CELERY_TASK_MAX_RETRIES = 3


WEATHER_API_KEY = env("WEATHER_API_KEY ")

CELERY_BEAT_SCHEDULE = {
    {
        "get_weather": {
            "task": "trace.shipment.tasks.get_weathers",
            "schedule": timedelta(hours=2),  # Run every 2 hours
            "args": [WeatherAPICaller(WEATHER_API_KEY)],
        },
    }
}
