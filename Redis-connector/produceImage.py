from google.cloud import pubsub_v1      # pip install google-cloud-pubsub  ##to install
import glob                             # for searching for json file 
import base64
import os 
import random
import numpy as np                      # pip install numpy    ##to install
import time
import traceback

# Search the current directory for the JSON file (including the service account key) 
# to set the GOOGLE_APPLICATION_CREDENTIALS environment variable.
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

# Set the project_id with your project ID
project_id="poetic-chariot-485605-h8";
topic_name = "Image2Redis";   # change it for your topic name if needed


# create a publisher and get the topic path for the publisher
publisher_options = pubsub_v1.types.PublisherOptions(enable_message_ordering=True)
publisher = pubsub_v1.PublisherClient( publisher_options=publisher_options)
topic_path = publisher.topic_path(project_id, topic_name)
print(f"Published messages with ordering keys to {topic_path}.")

with open("ontarioTech.jpg", "rb") as f:
    value =  base64.b64encode(f.read());   # read the image and serizalize it to base64

key="image";

try:    
    
    future = publisher.publish(topic_path, value, ordering_key=key);
    #ensure that the publishing has been completed successfully
    future.result()    
    print("The messages has been published successfully")
except Exception as e: 
    print("Failed to publish the message")
    print("ERROR:", repr(e))
    traceback.print_exc()
