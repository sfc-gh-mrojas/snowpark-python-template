from snowflake.snowpark.dataframe import DataFrame
import logging

def some_utility_method(df: DataFrame):
    """
    Dummy dataframe transformer
    """
    logging.warning("THIS IS A WARNING FROM MY UTILITY METHOD")
    logging.debug("Users may have existing log statements in their projects"+
                   " like this. Do they get collected into EVENT_TABLE?")

    return df