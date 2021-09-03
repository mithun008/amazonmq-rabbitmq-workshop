import sys

from routing_tasks import add, concat


def call_add(x, y):
    print("******** Calling add")
    add_result = add.delay(int(x), int(y))
    print(f"******** The result of adding {x} and {y}: {add_result.get()}")


def call_concat(x, y):
    print("******** Calling concat")
    concat_result = concat.delay(x, y)
    print(f"******** The result of concating {x} and {y}: {concat_result.get()}")


if __name__ == "__main__":
    call_add(*sys.argv[1:])
    call_concat(*sys.argv[1:])
