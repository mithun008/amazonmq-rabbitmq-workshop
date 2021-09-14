import sys
from random import randint

from priority_tasks import add


def call_add(x, y):
    for i in range(20):
        current_priority = randint(1, 10)
        current_x = randint(11, 711) + int(x)
        current_y = randint(44, 4444) + int(y)
        print(
            f"******** Calling add {current_x} and {current_y} with priority {current_priority}."
        )
        add.apply_async(
            (current_x, current_y, current_priority),
            queue="priority",
            priority=current_priority,
        )


if __name__ == "__main__":
    call_add(*sys.argv[1:])
