from pathlib import Path

import tests


def path(file_name):
    return str(
        Path(tests.__file__).parent.joinpath(f'file/{file_name}').absolute()
    )