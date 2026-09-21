"""Reusable data structures and functions for sales records."""


class SalesRecord:
    """Represent a sales record using a dictionary of field values."""

    def __init__(self, data):
        # Keep a separate dictionary so updates do not change the input.
        self.data = data.copy()

    def clean(self):
        """Remove surrounding whitespace from all string field values."""
        for field, value in self.data.items():
            if isinstance(value, str):
                self.data[field] = value.strip()

        return self

    def total(self):
        """Calculate revenue before any additional discounts."""
        return self.data["Unit Price"] * self.data["Units Sold"]


def build_sales_record(data):
    """Create a SalesRecord object from a dictionary."""
    return SalesRecord(data)