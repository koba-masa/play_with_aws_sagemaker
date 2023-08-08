import datetime
import boto3

def deploy():
    client = boto3.client('sagemaker')
    model = 'serverless-inference-202308052309'
    endpoint_config = create_endpoint_config(client, model)
    print(endpoint_config)
    update_endpoint(client, endpoint_config)


def create_endpoint_config(client, model_name):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M")
    response = client.create_endpoint_config(
        EndpointConfigName = f"serverless-inference-{timestamp}",
        ProductionVariants=  [
            {
                'VariantName': 'variant-1',
                'ModelName': model_name,
                'ServerlessConfig': {
                    'MemorySizeInMB': 6144,
                    'MaxConcurrency': 20,
                }
            }
        ],
        Tags = [
          {
              'Key': 'Project',
              'Value': 'play_with_aws_sagemaker'
          }
        ],
    )
    endpoint_config_arn = response['EndpointConfigArn']
    endpoint_config_name = endpoint_config_arn.split('/')[-1]
    return endpoint_config_name


def update_endpoint(client, endpoint_config):
    response = client.update_endpoint(
        EndpointName='play-with-aws-sagemaker-serverless-inference',
        EndpointConfigName=endpoint_config
    )

if __name__ == '__main__':
    deploy()
