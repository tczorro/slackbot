import os
import time
from slackclient import SlackClient
from command import command_dict
from sharemoney import _reference_cursor # reference to database using right now

bot_id = os.environ.get("BOT_ID")
at_bot = "<@" + bot_id + ">"

# slack bot key from local environment
slack_client = SlackClient(os.environ.get("SLACK_BOT_TOKEN"))

def handle_command(command, channel):
    # split command if the command is a phrase
    commands_split = command.split()
    main_command = commands_split[0] # main command key word
    else_command = commands_split[1:] # parameters for better run command
    response_func = command_dict.get("{}".format(main_command).lower())
    try:
        response = response_func(*else_command)
    except IndexError:
        response = "Incorrect command"
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
            print _reference_cursor
    else:
        print("Connection failed")
