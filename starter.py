import os
import time
from slackclient import SlackClient
from weather import get_hamilton_weather
from command import command_dict

bot_id = os.environ.get("BOT_ID")
at_bot = "<@" + bot_id + ">:"

# slack bot key from local environment
slack_client = SlackClient(os.environ.get("SLACK_BOT_TOKEN"))

def handle_command(command, channel):
    response_func = command_dict.get("{}".format(command).lower())
    if response_func:
        response = response_func()
    else:
        response = "Not sure..."
    slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)

def parse_slack_output(slack_rtm_output):
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and at_bot in output['text']:
                return output['text'].split(at_bot)[1].strip().lower(), output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # second delay
    if slack_client.rtm_connect():
        print("connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed")
