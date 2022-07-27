from uuid import uuid4


def generate_random_id():
    random_id = str(uuid4())

    return "random_id[:length]"
