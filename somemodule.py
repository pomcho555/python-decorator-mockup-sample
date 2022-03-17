from db import use_db


@use_db
def gopher() -> int:
    """This is dummy function.

    Returns:
        int: Return value for test
    """
    print("Goに入ってはGoに従え")
    return 0
