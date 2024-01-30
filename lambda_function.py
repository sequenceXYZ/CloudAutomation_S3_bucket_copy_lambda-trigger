import boto3

def lambda_handler(event, context):
    # Initialize S3 clients for source and destination buckets
    source_bucket_name = 'agnija-input-data'
    destination_bucket_name = 'agnija-output-data'
    
    s3_source = boto3.client('s3')
    s3_destination = boto3.client('s3')

    # Get the list of objects in the source bucket
    objects = s3_source.list_objects(Bucket=source_bucket_name)['Contents']

    # Iterate through each object in the source bucket
    for obj in objects:
        # Get the object key (filename)
        obj_key = obj['Key']

        # Copy the object from source to destination bucket
        copy_source = {'Bucket': source_bucket_name, 'Key': obj_key}
        destination_key = obj_key  # You can modify this if you want to change the destination key
        s3_destination.copy_object(Bucket=destination_bucket_name, CopySource=copy_source, Key=destination_key)

    return {
        'statusCode': 200,
        'body': 'Files copied successfully!'
    }
