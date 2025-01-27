# Pruebas con AWS Boto3

Este repositorio contiene ejemplos prácticos para interactuar con servicios de AWS utilizando el SDK de Python (Boto3). Incluye scripts para listar buckets, crear buckets y gestionar archivos en S3.

## Requisitos
- **Python** 3.9 o superior
- AWS CLI configurado para usar SSO con el IAM Identity Center

## Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/tuusuario/Ejemplos-Con-Boto3.git
   cd EjemploSDK

2. Crea un entorno virtual (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate       # En Linux/Mac
   venv\Scripts\activate          # En Windows

4. Instala las dependencias del proyecto:
   ```bash
   pip install -r requirements.txt

## Usos
1. Listar Buckets en S3
    ```bash
    python 01_listarBuckets.py

2. Crear un bucket en S3
    ```bash
    python 02_crearBuckets.py

3. Subir archivos a S3
    ```bash
    python 03_subirArchivos.py

4. Descargar archivos de S3
    ```bash
    python 04_bajarArchivos.py

## Estructura del proyecto
    
    EjemploSDK/
    ├── 01_listarBuckets.py  # Lista los buckets en tu cuenta de AWS
    ├── 02_crearBuckets.py   # Crea un nuevo bucket en S3
    ├── 03_subirArchivos.py  # Sube archivos al bucket
    ├── 04_bajarArchivos.py  # Descarga archivos desde S3
    ├── requirements.txt     # Dependencias del proyecto
    ├── .gitignore           # Archivos ignorados por Git
    └── venv/                # Entorno virtual (no incluido en el repositorio)

## Notas
  Estos ejemplos asumen que tienes el AWS CLI configurado con SSO para acceder a tus recursos en AWS.

   

