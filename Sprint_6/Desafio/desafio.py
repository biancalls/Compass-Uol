import boto3
from datetime import datetime
import os

# Definindo as variáveis de ambiente
AWS_ACCESS_KEY_ID = os.environ.get('ASIAXZEFHX2RBWH6ORPW')
AWS_SECRET_ACCESS_KEY = os.environ.get('HT8rsW0vxv5yQInkDwPGBXfy9oHbFTBwhNX6QiGh')
AWS_SESSION_TOKEN = os.environ.get('IQoJb3JpZ2luX2VjEHYaCXVzLWVhc3QtMSJIMEYCIQDSFki6v4PHm/ZnIA/DUn/yr7js65UZwm7YnNsTvF4nsQIhALbROLsKmDdHCYQSFWQH8bA87ljIjQNg8tFs2fx4U6eSKqYDCO///////////wEQABoMNTM1MDAyODU3MTIyIgxi4GgEtNE0cmL8D+Qq+gIJOxzuB0AmzrHLFRsC8jcAOzDjvIc+6ZpWqInij2A69hfQBmr63Crb+hZ0O0NRHEYK+QVgZMufl3XAmZGbD9/vmrhWPdohB2zNQ1P9HcH2ypdeDNFFGD/qNW/wa4C1rOvi3dgUlOG5Yy5IOKqXR2y9IQjYOgRU3YGERYOLKf/1wROYSAXbrdh4noSirPvRTVZDizqF+poNM1dEsp+3NYCdP/HRXN50J9RvguWudjwwsLuAhbphrwA1z4IqX8+GyqoNKXNEIKsNnUTViwrfA+xVaMhiKYtLd6rrXJOGdwgtqIHcu88XIEzj8UnTpKVx3U3zBVQflGKplfvLAj7ajAYGEN7OVV0TPwbrqD8PWUJ+f9g4zFsLslJIombnqIx+XFjRHrREYjoRXKa7aeXQdcBpun9iJSB28p+Idpr1eKvqhF6FhVEd6d0gjWejh2eCg5yid+7TsQBxEqxE/3/fCurjBDSlID72Gb/uVC2s9PC3EGCBE9BrSn342AkwuJ2juQY6pQEBP3VbTuW6FmntpUeSj1e2KaOzVIDvPOQqVxua9RDPuNf0poxLGJhiNffwFbZ80Nws0dV71PMnNnQG4E+qDhTps1OTUGPyZKqNSRE7itIAwwL+V9KFBCsZF0AGsG0cWMuBF7ubre+qOy+imba4roFd8yUv4gL01KJw2itONXf0vOMmePkgW7uRgtoox2cbNRozzvO8zanzdJbJPUwsdGiTSpRDkSU=')
# Criando a sessão do boto3
session = boto3.Session(
    aws_access_key_id='ASIAXZEFHX2RBWH6ORPW',
    aws_secret_access_key='HT8rsW0vxv5yQInkDwPGBXfy9oHbFTBwhNX6QiGh',
    aws_session_token='IQoJb3JpZ2luX2VjEHYaCXVzLWVhc3QtMSJIMEYCIQDSFki6v4PHm/ZnIA/DUn/yr7js65UZwm7YnNsTvF4nsQIhALbROLsKmDdHCYQSFWQH8bA87ljIjQNg8tFs2fx4U6eSKqYDCO///////////wEQABoMNTM1MDAyODU3MTIyIgxi4GgEtNE0cmL8D+Qq+gIJOxzuB0AmzrHLFRsC8jcAOzDjvIc+6ZpWqInij2A69hfQBmr63Crb+hZ0O0NRHEYK+QVgZMufl3XAmZGbD9/vmrhWPdohB2zNQ1P9HcH2ypdeDNFFGD/qNW/wa4C1rOvi3dgUlOG5Yy5IOKqXR2y9IQjYOgRU3YGERYOLKf/1wROYSAXbrdh4noSirPvRTVZDizqF+poNM1dEsp+3NYCdP/HRXN50J9RvguWudjwwsLuAhbphrwA1z4IqX8+GyqoNKXNEIKsNnUTViwrfA+xVaMhiKYtLd6rrXJOGdwgtqIHcu88XIEzj8UnTpKVx3U3zBVQflGKplfvLAj7ajAYGEN7OVV0TPwbrqD8PWUJ+f9g4zFsLslJIombnqIx+XFjRHrREYjoRXKa7aeXQdcBpun9iJSB28p+Idpr1eKvqhF6FhVEd6d0gjWejh2eCg5yid+7TsQBxEqxE/3/fCurjBDSlID72Gb/uVC2s9PC3EGCBE9BrSn342AkwuJ2juQY6pQEBP3VbTuW6FmntpUeSj1e2KaOzVIDvPOQqVxua9RDPuNf0poxLGJhiNffwFbZ80Nws0dV71PMnNnQG4E+qDhTps1OTUGPyZKqNSRE7itIAwwL+V9KFBCsZF0AGsG0cWMuBF7ubre+qOy+imba4roFd8yUv4gL01KJw2itONXf0vOMmePkgW7uRgtoox2cbNRozzvO8zanzdJbJPUwsdGiTSpRDkSU='
)

s3 = session.resource('s3')

s3_client = session.client('s3')

nome_bucket = 'datalake.biancalages'

s3_client.create_bucket(Bucket=nome_bucket)

path_arq1= r"/app/series.csv"
path_arq2= r"/app/movies.csv"

nome_arq1 = r"series.csv"
nome_arq2 = r"movies.csv"

data = datetime.now().strftime("%d/%m/%Y")

path_series = f"RAW/Local/CSV/Series/{data}/{nome_arq1}"
path_moveis = f"RAW/Local/CSV/Movies/{data}/{nome_arq2}"

s3_client.upload_file(path_arq1, nome_bucket, path_series)
s3_client.upload_file(path_arq2, nome_bucket, path_moveis)

print(f'Upload do arquivo {nome_arq1} e {nome_arq2}')



