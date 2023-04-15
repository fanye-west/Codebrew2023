# ryde-api built using AWS SAM (Serverless Application Model)

This directory contains source code and code used to define and deploy AWS cloud resoruceses for our API.

This project contains source code and supporting files for the Ryde serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- hello_world - Code for the application's testing/initial Lambda function.
- lambda_handlers - Code for the application's business logic Lambda function.
- template.yaml - A template that defines the application's AWS resources.

The application uses several AWS resources, including Lambda functions and an API Gateway API. These resources are defined in the `template.yaml` file in this project. 

## Deploy the Ryde application
To deploy you must use the SAM CLI, you need the following tools.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)

To build and deploy the application for the first time, run the following:

```bash
sam build --use-container
sam deploy --guided
```


