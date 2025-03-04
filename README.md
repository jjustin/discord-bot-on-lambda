# discord-bot-on-lambda

> Based on: <https://github.com/ker0olos/aws-lambda-discord-bot>

An example discord bot that can be deployed to AWS lambda.

## Requires

- Docker
- [mise](https://mise.jdx.dev/) for tooling installation
- Configured AWS credentials with an existing Lambda function
  - [aws-vault](<https://github.com/99designs/aws-vault>) can be used for the credentials part

## Deploy

To deploy a new version of the bot to AWS Lambda run:

```sh
task deploy
```

The task will take care of:

- fetching the required pip packages for Amazon Linux.
- generating the package zip
- pushing the package zip to AWS
- setting the env variables for the Lambda function

## Update

The available commands need to be pushed to discord when bot is updated. Use `update.py` for that.
