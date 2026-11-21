import boto3

# Set your endpoint name
endpoint_name = "sagemaker-scikit-learn-2026-11-21-10-57-52-044"
region = "us-east-1"

# Input as plain CSV string
#csv_input = "5.2,3.0,1.4,0.6"
csv_input = "5.8,2.7,5.1,1.9"

# Initialize runtime client
runtime = boto3.client("sagemaker-runtime", region_name=region)

# Invoke the endpoint
response = runtime.invoke_endpoint(
    EndpointName=endpoint_name,
    ContentType="text/csv",
    Body=csv_input
)

# Read and print prediction
print("🧠 Prediction:", response["Body"].read().decode())
