
import pytest
from snowflake.snowpark.session import Session
from src.util.local import get_env_var_config

@pytest.fixture
def session():
    # We need an active session for the @udf decorator
    return Session.builder.configs(get_env_var_config()).create()

def test_combine(session):
    from src.udf.functions import combine  # udf must be imported here so that an active session is available. Importing at the top does not work
    expected = "hello world"
    actual = combine("hello ", "world")
    #assert expected == actual
