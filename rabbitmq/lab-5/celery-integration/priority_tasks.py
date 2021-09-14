from time import sleep

from kombu import Exchange, Queue

from base_app import get_base_celery_app

app = get_base_celery_app(module_name="prority_tasks")

app.conf.task_queues = [
    Queue(
        "priority",
        Exchange("priority"),
        routing_key="priority",
        queue_arguments={"x-max-priority": 10},
    )
]
app.conf.task_acks_late = True
app.conf.worker_prefetch_multiplier = 1
app.conf.task_ignore_result = True


@app.task()
def add(x, y, priority):
    sleep(2)
    return f"priority {priority}"
