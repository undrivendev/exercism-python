import random


class Robot:
    """Represents the robot class.

    Args:
        name: 
            A string generated with a specific 
            format during initialization and when the method
            reset() is called.
    """

    name = ""

    def __init__(self):
        """Initializes the 'name' field with a random value."""
        self.name = self.generate_random_name()

    def generate_random_name(self) -> str:
        """Generates a random name following a specific format.

        The format used to create the random name is composed by
        two letters followed by 3 digits. Examples: AB123, LS104.

        Returns:
            The generated name.
        """
        valid_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        r = random.Random()
        return f"{valid_letters[r.randint(0, 25)]}{valid_letters[r.randint(0, 25)]}{r.randint(0, 999):03d}"

    def reset(self):
        """Sets the 'name' field to a new random value."""
        self.name = self.generate_random_name()
