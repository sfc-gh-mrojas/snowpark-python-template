"""
Tests for the procedure module.
"""
import os
from snowflake.snowpark.session import Session
from app import run


def test_app_dim(session: Session):
    import functions
    session.add_import(functions.__file__, 'functions')
    expected = session.create_dataframe(
        [["Welcome to Snowflake!"], ["Learn more: https://www.snowflake.com/snowpark/"]],
        ["hello_world"])
    
    actual = run(session)

    assert expected.collect() == actual.collect()
