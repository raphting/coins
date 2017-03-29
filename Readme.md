GCloud mock bitcoin miner
=========================

This software is an example on how to use google's cloud for
mining bitcoins in a mock implementation.

Installation
------------

You need python2.7 and pip
Install the requirements with pip install -r ./requirements.txt

Environment
-----------

In order to connecto to googles pub/sub, you need to create two topics
with one subscription each first.

Topic: PUBSUB_WORK Subscription: PUBSUB_TASK

Distributes the work tasks.


Topic: PUBSUB_STATUS Subscription: PUBSUB_SOLUTION

Fetches succesful work tasks.

Set the Topic and Subscription names as environment variables as well.

