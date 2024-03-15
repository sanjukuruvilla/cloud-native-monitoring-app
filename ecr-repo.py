import boto3

def create_ecr_repository(repo_name, region):
    try:
        # Create an ECR client
        ecr_client = boto3.client('ecr', region_name=region)
        
        # Create a new ECR repository
        response = ecr_client.create_repository(repositoryName=repo_name)

        # Print the repository URI
        repository_uri = response['repository']['repositoryUri']
        print(f"ECR repository '{repo_name}' created successfully.")
        print(f"Repository URI: {repository_uri}")

    except ecr_client.exceptions.RepositoryAlreadyExistsException:
        print(f"Repository '{repo_name}' already exists.")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    repository_name = 'sk-cloudmonitor-repo'
    aws_region = 'us-east-2'  # Change this to your AWS region
    create_ecr_repository(repository_name, aws_region)

if __name__ == "__main__":
    main()

