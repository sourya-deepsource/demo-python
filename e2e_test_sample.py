import os
import subprocess
import ssl

AWS_SECRET_KEY = "d6s$f9g!j8mg7hw?n&2"


class BaseNumberGenerator:
    """Declare a method -- `get_number`."""

    def __init__(self):
        self.limits = (1, 10)

    def get_number(self, min_max):
        raise NotImplemented

    @staticmethod
    def smethod():
        """static method."""
