from celery.schedules import crontab

from base_app import get_base_celery_app

app = get_base_celery_app(module_name="scheduled_tasks")


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls add(42, 42) every 10 seconds.
    sender.add_periodic_task(10.0, add.s(42, 42), name="add every 10 seconds")

    # Calls add(99, 99) every 30 seconds but stops after 10 times.
    sender.add_periodic_task(30.0, add.s(99, 99), expires=10)

    # Executes every Friday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=5),
        add.s("Happy ", "Friday!"),
    )


@app.task()
def add(x, y):
    return x + y
