This script creates or updates the Lambda function and prints its details in JSON format, providing a structured output of your Lambda function configuration.
Notes :
--> Replace your_access_key_id, your_secret_access_key, YOUR_ACCOUNT_ID, and YourLambdaExecutionRole with your actual AWS credentials, account details, and IAM role name.

------------------------------------------------------------------------------------------ Explanation -----------------------------------------------------------------------------------

Lambda Function Code: The lambda_code variable contains the code for your Lambda function.

Writing Code to File: The script writes this code to lambda_function.py.

Creating a Zip File: The script creates a zip file (lambda_function.zip) containing lambda_function.py.

Reading Zip File Content: The script reads the content of the zip file into a variable zip_file_content.

Creating or Updating the Lambda Function: 
The script creates or updates the Lambda function by directly providing the zip_file_content to the create_function and update_function_code methods.
The role is specified here. Make sure YourLambdaExecutionRole exists and has the necessary permissions for Lambda execution.

Cleaning Up: The script deletes the temporary files (lambda_function.py and lambda_function.zip).

Outputting Details in JSON Format: The script retrieves the Lambda function details using get_function and prints them in JSON format.
