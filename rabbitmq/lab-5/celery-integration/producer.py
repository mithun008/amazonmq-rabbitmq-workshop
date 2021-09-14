import sys

from simple_tasks import add


def call_add(x, y):
    result = add.delay(int(x), int(y))
    print(f"******** The result of adding {x} and {y}: {result.get()}")


if __name__ == "__main__":
    call_add(*sys.argv[1:])
