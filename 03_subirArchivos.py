import logging
import boto3
from botocore.exceptions import ClientError
import os

# Configurar logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

session = boto3.Session(profile_name="AdministratorAccess-376129873205")

objeto_s3 = session.resource('s3')

def upload_file(file_name, bucket, object_name):
    """Subir un archivo a un bucket S3 donde:
        file_name: nombre del archivo a subir
        bucket: nombre del bucket que lo va a alojar
        object_name: un nombre para el objeto (archivo) a subir. Si no se especifica, queda igual que file_name
        
        La función devuelve true si se pudo subir, caso contrario devuelve false"""
    
    # Si objet_name no fue especificado usar file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Subir el archivo
    s3_client = session.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
        logging.info(f"El archivo '{file_name} fue subido con éxito al bucket '{bucket}")

    except ClientError as err:
        logging.info(f"\n\nNo se pudo subir el archivo debido al error:\n\n{err}")        
        return False
    return True

nombreDelArchivo = input("\nIngrese el nombre del archivo a subir: ")

print("\n\nActualmente existen los siguientes buckets:")

for elem in objeto_s3.buckets.all():
    print(elem)

nombreDelBucket = input("\nIngrese el nombre del bucket a utilizar: ")

nombreDelObjeto = None

upload_file(nombreDelArchivo, nombreDelBucket, nombreDelObjeto)