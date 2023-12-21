import boto3




# # Instantiate a table resource object without actually
# # creating a DynamoDB table. Note that the attributes of this table
# # are lazy-loaded: a request is not made nor are the attribute
# # values populated until the attributes
# # on the table resource are accessed or its load() method is called.
# table = dynamodb.Table("BackendStack-TableCD117FA1-WVKEL3KI1DML")
# print(table.creation_date_time)

import os
import logging

def get_env(env_var_name: str) -> str:
    if env_var := os.getenv(env_var_name):
        return env_var
    else:
        logging.error(f"{env_var_name} is needed")
        raise ValueError(f"{env_var_name} is needed")
        


def handler(context, event):
    TABLE_NAME: str = get_env("TABLE_NAME")
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(TABLE_NAME)
    print(table.creation_date_time)
    print(f"{context=} {event=}")
    return os.environ['TABLE_NAME']