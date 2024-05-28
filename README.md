# Fortune-Teller-AWS-

Creating a fortune teller application using AWS Lambda and API Gateway involves several steps. The general flow includes setting up an API Gateway to handle HTTP requests, configuring a Lambda function to process these requests, and then returning a fortune-telling response. Here's a step-by-step guide to get you started:

Step 1: Setting Up AWS Lambda
Create a Lambda Function:

Go to the AWS Management Console.
Navigate to the Lambda service.
Click on "Create function".
Choose "Author from scratch".
Give your function a name (e.g., FortuneTellerFunction).
Choose the runtime (e.g., Python 3.8).
Click "Create function"

Add Code to Lambda Function
Save the Lambda Function.

Step 2: Setting Up API Gateway
Create an API:

Go to the API Gateway service in the AWS Management Console.
Click on "Create API".
Choose "REST API" and then "Build".
Configure the API:

Give your API a name (e.g., FortuneTellerAPI).
Click "Create API".
Create a Resource and Method:

In the API Resources panel, click on "Actions" and select "Create Resource".
Give the resource a name (e.g., fortune).
Click "Create Resource".
With the new resource selected, click on "Actions" and select "Create Method".
Choose "GET" and click the checkmark.
Integrate GET Method with Lambda:

In the GET method setup, select "Lambda Function" as the integration type.
Check the "Use Lambda Proxy integration" box.
In the Lambda Function box, type the name of your Lambda function (e.g., FortuneTellerFunction).
Click "Save" and then "OK" to grant API Gateway permission to invoke your Lambda function.
Step 3: Deploy the API
Deploy the API:

Click on "Actions" in the API Resources panel and select "Deploy API".
Create a new stage (e.g., prod).
Click "Deploy".
Get the Invoke URL:

After deployment, you will see the Invoke URL (e.g., https://<api-id>.execute-api.<region>.amazonaws.com/prod/fortune).
Step 4: Test the API
You can test your API using a browser or a tool like Postman. For example, to get a fortune for a specific question, you can use the following URL format
