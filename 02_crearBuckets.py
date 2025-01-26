import logging
import boto3
from botocore.exceptions import ClientError

# La libería logging es nativa de Python que según la documentación implementa funciones y clases que implementa un sistema
# de logueo de eventos.
# Al instalar boto3 (el AWS Python SDK) se instala automaticamente la librería botocore (es una dependencia de boto3).
# La misma es la encargada de generar excepciones relacionadas con comportamientos del lado del cliente, 
# configuracione y validaciones

# Configurar logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# Especifico mi sesión de para el usuario del IAM Identity Center (SSO)
session = boto3.Session(profile_name="AdministratorAccess-376129873205")

# Creo un objeto s3 para para poder trabajar sobre el mismo (no es necesario para la creación de un bucket)
recurso_s3 = session.resource('s3')

def create_bucket(bucket_name, region):
    """Crear un bucket en una región especificada.
    
    Si no se especifica una región, se crea el bucket por default en us-east-1
    :param bucket_name: el bucket que se va a crear
    :param region: string de la region para crear el bucket
    :return: True si se creó o bucket sino return False"""

    # Crear bucket
    try:
        # Crear cliente de S3 en la región ingresada sino toma us-east-1 por default
        s3_client = session.client('s3', region_name = region if region else "us-east-1")
        
        if not region or region == "us-east-1":

            #Crear bucket en region us-east-1
            s3_client.create_bucket(Bucket = bucket_name)

        else:
            # Caso contrario crear bucket en la región seleccionada
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket = bucket_name, CreateBucketConfiguration = location)

        logging.info(f"\n\nEl bucket '{bucket_name}' fue creado con éxito en la región '{region}'")
        
        # Lista los buckets llamando al objeto s3 creado inicialmente
        print("\nLos buckets creados hasta el momento son:")
   
        for elem in recurso_s3.buckets.all():
            print(elem.name)

    except ClientError as err:
        logging.error(f"\n\nSe produjo el siguiente error intentando crear el bucket:\n\n{err}")
        return False
    return True

# Pido al usuario que ingrese un nombre para el bucket. 
# El método strip() para strings elimina los espacios en blanco
nombreDelBucket = input("\nIngrese nombre del bucket: ").strip()

# Pido al usuario que ingrese un nombre para el bucket. 
# Uso también el método strip() o asigno None si no se ingresa nada
nombreDeRegion = input("\nIngrese región: ").strip() or None

# Llamo a la función y le paso como parámetro los datos ingresados por el usuario
create_bucket(nombreDelBucket, nombreDeRegion)

