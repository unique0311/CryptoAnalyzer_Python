import os


def Get_Source_Root():
    """
    Returns the root director of the project
    :return: The root director of the project
    """
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
