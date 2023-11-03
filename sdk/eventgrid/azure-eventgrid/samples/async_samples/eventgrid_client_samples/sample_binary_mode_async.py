# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import os
import asyncio
import json
from azure.core.credentials import AzureKeyCredential
from azure.eventgrid.aio import EventGridClient
from azure.eventgrid.models import *
from azure.core.messaging import CloudEvent
from azure.core.exceptions import HttpResponseError


EVENTGRID_KEY: str = os.environ["EVENTGRID_KEY"]
EVENTGRID_ENDPOINT: str = os.environ["EVENTGRID_ENDPOINT"]
TOPIC_NAME: str = os.environ["EVENTGRID_TOPIC_NAME"]
EVENT_SUBSCRIPTION_NAME: str = os.environ["EVENTGRID_EVENT_SUBSCRIPTION_NAME"]

# Create a client
client = EventGridClient(EVENTGRID_ENDPOINT, AzureKeyCredential(EVENTGRID_KEY))


async def run():
    async with client:
        # Publish a CloudEvent
        try:
            # Publish CloudEvent in binary mode with str encoded as bytes
            cloud_event_dict = {"data":b"HI", "source":"https://example.com", "type":"example", "datacontenttype":"text/plain"}
            await client.publish_cloud_events(topic_name=TOPIC_NAME, body=cloud_event_dict)

            # Publish CloudEvent in binary mode with json encoded as bytes
            cloud_event = CloudEvent(data=json.dumps({"hello":"data"}).encode("utf-8"), source="https://example.com", type="example", datacontenttype="application/json")
            await client.publish_cloud_events(topic_name=TOPIC_NAME, body=cloud_event, binary_mode=True)

            receive_result = await client.receive_cloud_events(
                topic_name=TOPIC_NAME,
                event_subscription_name=EVENT_SUBSCRIPTION_NAME,
                max_events=10,
                max_wait_time=10,
            )
            for details in receive_result.value:
                cloud_event_received = details.event
                print("CloudEvent: ", cloud_event_received)
                print("Data: ", cloud_event_received.data)
        except HttpResponseError:
            raise

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(run())
