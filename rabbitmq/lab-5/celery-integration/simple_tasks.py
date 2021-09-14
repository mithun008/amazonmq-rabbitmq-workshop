from base_app import get_base_celery_app

app = get_base_celery_app(module_name="simple_tasks")


@app.task()
def add(x, y):
    return x + y
