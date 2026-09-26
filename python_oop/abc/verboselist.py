#!/usr/bin/env python3
"""Defines a VerboseList class that extends the built-in list."""


class VerboseList(list):
    """A list that prints a message when it is modified."""

    def append(self, item):
        """Add an item and notify."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Add several items and notify."""
        items = list(iterable)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Notify, then remove an item."""
        if item in self:
            print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Remove an item at index and notify."""
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return item
