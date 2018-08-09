from typing import Any, Dict

from flask import Flask

import boto3

from app.schema import EventSchema


class EventClientException(Exception):
    def __init__(self, message: str = 'Event client failed.') -> None:
        super().__init__(message)


class EventClient:

    def init_app(self, app: Flask) -> None:
        return self.init(app.config)

    def init(self, config: Dict[str, Any]) -> None:
        self.client = boto3.client(
            'sns',
            region_name=config['AWS_REGION_NAME'],
            aws_access_key_id=config['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=config['AWS_SECRET_ACCESS_KEY']
        )
        self.queue_topic = self._get_topic_by_name(config['SNS_TOPIC_NAME'])

    def send_event(self, event: EventSchema) -> Dict[str, Any]:
        return self.client.publish(
            TopicArn=self.queue_topic,
            MessageAttributes={
                'event_type': {
                    'DataType': 'String',
                    'StringValue': event['event_type']
                },
            },
            Message=event['data']
        )

    def _get_topic_by_name(self, topic_name: str) -> str:
        try:
            return next(
                topic['TopicArn']
                for topic in self.client.list_topics()['Topics']
                if topic['TopicArn'].split(":")[-1] == topic_name
            )
        except StopIteration as e:
            raise EventClientException(
                "Could not get topic arn from topic name {}".format(topic_name)
            ) from e


client = EventClient()
