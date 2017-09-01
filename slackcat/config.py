import os

webhook_url = os.environ.get('SLACKCAT_WEBHOOK_URL')
username = os.environ.get('SLACKCAT_USERNAME', 'slackcat')
icon_url = os.environ.get('SLACKCAT_ICON_URL')
