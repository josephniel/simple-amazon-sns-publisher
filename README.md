# Simple Amazon SNS Publisher


## Description
This repository serves as a basic wrapper for SNS message publishing.

## Installation
Create an `.env` file in the root directory with proper config values. (i.e. use `.env.template` as your guide for necessary attributes to include). After, you can simply
```
docker-compose up --build
```
to build and run the container.

## Endpoint
```
POST /events

{
    'event_type': <queue_identifier>,
    'data': <payload>
}
```
The `event_type` serves as an identifier for the SNS queue to filter messages. The `data` is the main payload for the event.

## Amazon Setup
This wrapper assumes that there is already an SNS topic created (and defined in the `.env` file) and SQS queues are aleady subscribed to the topic. We only need to do the following per queue subscription to be able to utilize the `event_type` property of the wrapper:

```
{
    "event_type": ["sample_type"]
}
```
More of setting up the filtering [here](https://aws.amazon.com/getting-started/tutorials/filter-messages-published-to-topics/). Filter structure can be found [here](https://docs.aws.amazon.com/sns/latest/dg/message-filtering.html).
