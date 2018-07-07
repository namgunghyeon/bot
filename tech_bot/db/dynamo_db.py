import boto3
from datetime import datetime
from db.singleton import Singleton
from db.db import DB
from config import AWSConfig
from config import DBConfig

class DynamoDB(DB):
    __metaclass__ = Singleton
    def __init__(self):
      self._session = boto3.Session(
          aws_access_key_id = AWSConfig.aws_access_key_id,
          aws_secret_access_key = AWSConfig.aws_secret_access_key,
          region_name = AWSConfig.region_name
      )

      self._dynamodb = self._session.resource("dynamodb")
      self._init_table()

    def _init_table(self):
      try:
        self._table = self._dynamodb.Table(DBConfig.table_name)
        self._table.creation_date_time

      except Exception as e:
        if (type(e).__name__ == "ResourceNotFoundException"):
          create_table = self._dynamodb.create_table(
            TableName=DBConfig.table_name,
            KeySchema=[
              {
                "AttributeName": "site",
                "KeyType": "HASH",
              },
            ],
            AttributeDefinitions=[
              {
                "AttributeName": "site",
                "AttributeType": "S",
              },
            ],
            ProvisionedThroughput={
              "ReadCapacityUnits": 1,
              "WriteCapacityUnits": 1
            }
        )
        create_table.meta.client.get_waiter('table_exists').wait(TableName=DBConfig.table_name)

      finally:
        self._table = self._dynamodb.Table(DBConfig.table_name)

    def get(self, site):
      response = self._table.get_item(Key={
        "site": site
      })

      if 'Item' not in response:
        return None

      item = response["Item"]

      return {
        "site": item["site"],
        "title": item["title"],
        "link": item["link"],
        "date": item["date"]
      }

    def save(self, site, title, link):
      self._table.put_item(
        Item={
              "site": site,
              "title": title,
              "link": link,
              "date": str(datetime.now())
          }
      )
