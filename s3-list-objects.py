import boto3
import pandas

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
prefix = '' ## folder name or path
# connect to s3
s3 = boto3.client(
's3',
aws_access_key_id=AWS_ACCESS_KEY_ID,
aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)

# Create a client
client = boto3.client('s3', region_name='us-west-2')

# Create a reusable Paginator
paginator = client.get_paginator('list_objects_v2')

# Create a PageIterator from the Paginator
page_iterator = paginator.paginate(Bucket='', Prefix=prefix)
                                   ##PaginationConfig={'MaxItems': 1000})
listOfObject = []
for page in page_iterator:
    #print(page['Contents'])
    for obj in page['Contents']:
        # list key of object
        listOfObject.append(obj['Key'])
        #print(obj['Key'])

    
#print(listOfObject)

# list to DataFrame
listDataFrame = pandas.DataFrame(listOfObject)
# export to csv
listDataFrame.to_csv(prefix+'list.csv')
