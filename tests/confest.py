import os
import pytest
from django.conf import settings


@pytest.fixture(autouse=True)
def enable_db_access(db):
    pass
