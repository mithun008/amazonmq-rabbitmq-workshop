from base_app import get_base_celery_app

app = get_base_celery_app(module_name="routing_tasks")

app.conf.task_routes = {"routing_tasks.concat": {"queue": "concat_queue"}}


@app.task()
def add(x, y):
    return x + y


@app.task()
def concat(x, y):
    return str(x) + " " + str(y) + "!"
