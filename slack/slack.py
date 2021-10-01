import slackweb, config

slack = slackweb.Slack(url=config.slack_url)
slack.notify(text="pythonからslackさんへ")