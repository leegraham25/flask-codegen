import os


def log(message):
    # TODO: Do something so that `--verbose` actually does something
    print(message)


def create_dir(path):
    """Wrapper around os.mkdir to allow dryrun functionality"""
    # TODO: Handle `--dry-run` somehow
    if os.path.exists(path):
        return

    os.mkdir(path)
