import os
import logging
import random
import time

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk import WebClient

from db import Database
import freee
from message import Message


logging.basicConfig(level=logging.WARNING)


app = App(token=os.environ["SLACK_BOT_TOKEN"])
client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])


@app.message("^.*<@{}>.*$".format(os.environ["SLACK_USER_ID"]))
def message(message):
    
    if freee.is_working():
        return


    client.chat_postMessage(channel=message["channel"], text= "すみません、稼働しておりません。稼働しましたら返信いたします。")


if __name__ == "__main__":
    Database.initialise()

    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()
