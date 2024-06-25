import json
import boto3
import zipfile
import os


# Define the function code
lambda_code = """
import json

def lambda_handler(event, context):
    number1 = event.get('number1', 0)
    number2 = event.get('number2', 0)
    result = number1 + number2
    return {
        'statusCode': 200,
        'body': json.dumps({'result': result})
    }
"""

# Write the Lambda function code to a file
with open('lambda_function.py', 'w') as f:
    f.write(lambda_code)

# Create a zip file containing the Lambda function code
with zipfile.ZipFile('lambda_function.zip', 'w') as z:
    z.write('lambda_function.py')

# Function name
function_name = 'MyLambdaFunction'    

# Initialize a Boto3 session with AWS credentials and region
aws_access_key_id = 'your_access_key_id'
aws_secret_access_key = 'your_secret_access_key'
region_name = 'us-east-1'

session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)
client = session.client('lambda')

# Create or update the Lambda function
try:
    response = client.create_function(
        FunctionName= function_name,
        Role='arn:aws:iam::YOUR_ACCOUNT_ID:role/service-role/YourLambdaExecutionRole',
        Runtime='python3.8',
        Handler='lambda_function.lambda_handler',
        Code={'ZipFile': open('lambda_function.zip', 'rb').read()},
        Description='A simple lambda function that adds two numbers',
        Timeout=30,
        MemorySize=128,
        Publish=True,
    )
    print(f"Lambda function created successfully: {response['FunctionArn']}")
except client.exceptions.ResourceConflictException:
    print("The function already exists. Updating the existing function...")
    response = client.update_function_code(
        FunctionName= function_name,
        ZipFile=open('lambda_function.zip', 'rb').read(),
        Publish=True,
    )
    print(f"Lambda function updated successfully: {response['FunctionArn']}")

# Clean up the temporary files
os.remove('lambda_function.py')
os.remove('lambda_function.zip')

# Output Lambda function details in JSON format
if response:
    function_details = client.get_function(FunctionName=function_name)
    print(json.dumps(function_details, indent=4, default=str))