import sys

from simple_tasks import add


def call_add(x, y):
    result = add.apply_async((int(x), int(y)), countdown=120)
    print(f"******** The result of adding {x} and {y}: {result.get()}")


if __name__ == "__main__":
    call_add(*sys.argv[1:])
