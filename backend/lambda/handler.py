# import boto3


# dynamodb = boto3.resource("dynamodb")

# # Instantiate a table resource object without actually
# # creating a DynamoDB table. Note that the attributes of this table
# # are lazy-loaded: a request is not made nor are the attribute
# # values populated until the attributes
# # on the table resource are accessed or its load() method is called.
# table = dynamodb.Table("BackendStack-TableCD117FA1-WVKEL3KI1DML")
# print(table.creation_date_time)

import os

def handler(context, event):
    print(f"{os.environ['TABLE_NAME']=}")
    print(f"{context=} {event=}")
    return os.environ['TABLE_NAME']