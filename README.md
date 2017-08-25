
<p align="center">
  <img src="https://s3.amazonaws.com/assets.nickficano.com/slackcat.svg" height="64">
  <h2 align="center">SlackCat</h3>
  <p align="center">Concatenate files(s), or <code>stdin</code>, directly to Slack.<br>
  3-minute setup & no third-party integration required.
<p align="center">
<a href="https://pypi.python.org/pypi/slackcat/"><img src="https://img.shields.io/pypi/pyversions/slackcat.svg" alt="pypi"></a>
<a href="https://pypi.python.org/pypi/slackcat/"><img src="https://img.shields.io/pypi/v/slackcat.svg" alt="pypi"></a>
<img src="https://img.shields.io/badge/pip_dependencies-0-brightgreen.svg" alt="pip dependencies">
</p>
 </p>

### Get SlackCat

Download using pip via pypi.

```bash
pip install slackcat
```

Next, head to the [Slack Incoming WebHooks Configuration](https://slack.com/apps/A0F7XDUAZ-incoming-webhooks), click
the ``Add Configuration`` button and set the default configuration values to your
liking. Once complete, copy the Webhook URL which we'll need in the next step.

Open your ``~/.bash_profile`` file add following:

```bash

export SLACKCAT_WEBHOOK_URL="https://hooks.slack.com/services/TXXX/BXXXX/XXXXXXXXXXXXXXXXXXXXXXXX"
```

_Make sure to replace the "https://hooks.slack.com/services/..." with the one provided above._

### Usage

```bash

# "Hey what's your public key dog?"
slackcat @doug ~/.ssh/id_rsa.pub

# "Do we still use that crypto library written by the Cheese Cake Factory?"
grep -r 'from cheesecake.factory import x509' ./ | slackcat @paul

# Send to a channel
echo $PATH | slackcat "#general"
```

### Customization

If you would like to override the bot's username, add the following line to your ``~/.bash_profile`` file:

```bash

export SLACKCAT_USERNAME="abraham-linksys"
```

If you would like to override the bot's icon image, add the following line to your ``~/.bash_profile`` file:

```bash

export SLACKCAT_ICON_URL="http://via.placeholder.com/500x500.png"
```

### Development
Development of "SlackCat" is facilitated exclusively on GitHub. Contributions in the form of patches, tests and feature creation and/or requests are very welcome and highly encouraged. Please open an issue if this tool does not function as you'd expect.

**How to release updates**

If this is the first time you're releasing to pypi, you'll need to run: ``pip install -r tests/dev_requirements.txt``.

Once complete, execute the following commands:

```bash

git checkout master

# Increment the version number and tag the release.
bumpversion [major|minor|patch]

# Upload the distribution to PyPi
python setup.py sdist bdist_wheel upload

# Since master often contains work-in-progress changes, increment the version to a patch release to prevent inaccurate attribution.
bumpversion --no-tag patch

git push origin master --tags
```
