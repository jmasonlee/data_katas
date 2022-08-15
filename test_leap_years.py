import pytest

from main import leap_years

"""
For example, 2001 is a typical common year and 1996 is a typical leap year, whereas 1900 is an atypical common year and 2000 is an atypical leap year.
"""

# Input of 2001, Output of False
def test_typical_common_year():
    assert leap_years(2001) == False

# Input of 1996, Output of True

# Input of 1900, Output of False

# Input of 2000, Output of True





