import boto3
import logging
from botocore.exceptions import ClientError

# Configurar logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

session = boto3.Session(profile_name="AdministratorAccess-376129873205")
s3_client = session.client('s3')
s3_object = session.resource('s3')

# Listar todos los buckets
print("\nLa lista de buckets es:")
for elem in s3_object.buckets.all():
    print(elem.name)

nombreDelBucket = input("\nSeleccione un bucket de la lista: ")

# Listar todos los objetos (archivos) dentro del bucket elegido
print(f"\nLa lista de archivos en el bucket '{nombreDelBucket}' es: ")

bucketElegido = s3_object.Bucket(nombreDelBucket)

for file in bucketElegido.objects.all():
    print(file.key)

nombreDelArchivo = input("\nSeleccione un archivo de la lista: ")

# Asigno el nomnbre del archivo a la variable del nombre del objeto para simplificar el input
# No siempre van a ser iguales dado que el objeto puede tener un nombre distinto al archivo.
nombreDelObjeto = nombreDelArchivo

def bajarArchivo(nombreDelBucket, nombreDelObjeto, nombreDelArchivo):
    try:
        s3_client.download_file(nombreDelBucket, nombreDelObjeto, nombreDelArchivo)
        logging.info(f"\nEl archivo '{nombreDelArchivo} fue descargado correctamente")

    except ClientError as err:
        logging.info(f"\nEl archivo '{nombreDelArchivo} no se pudo descargar debido al error: {err}")
        return False    
    return True


bajarArchivo(nombreDelBucket, nombreDelObjeto, nombreDelArchivo)
