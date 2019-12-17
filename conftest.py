import pytest
import datetime as dt
import os
from fixture.helper import *
from model.input_data import *

@pytest.fixture
def fix():
    fixture = Helper()
    return fixture
