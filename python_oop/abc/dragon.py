#!/usr/bin/env python3
"""Demonstrates mixins with a Dragon class."""


class SwimMixin:
    """Mixin that adds swimming ability."""

    def swim(self):
        """Print that the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying ability."""

    def fly(self):
        """Print that the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represents a dragon that can swim and fly."""

    def roar(self):
        """Print that the dragon roars."""
        print("The dragon roars!")
