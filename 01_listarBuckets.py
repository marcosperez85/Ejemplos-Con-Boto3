import boto3

# Especifica el perfil configurado
session = boto3.Session(profile_name="AdministratorAccess-376129873205")
s3 = session.resource('s3')

# Lista los buckets
for elem in s3.buckets.all():
    print(elem.name)
