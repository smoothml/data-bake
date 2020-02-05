from contextlib import contextmanager
from cookiecutter.utils import rmtree


@contextmanager
def bake_in_temp_dif(cookiesm, *args, **kwargs):
    result = cookies.bake(*args, **kwargs)

    try:
        yield result
    finally:
        rmtree(str(result.project))
