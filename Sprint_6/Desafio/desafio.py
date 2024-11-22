import boto3
from datetime import datetime
import os

# Definindo as variáveis de ambiente
AWS_ACCESS_KEY_ID = os.environ.get('ASIAXZEFHX2RON5Y5X52')
AWS_SECRET_ACCESS_KEY = os.environ.get('X6OBIYjYHMApAny2tMi5BbaiEfWLB474yOYEZhCU')
AWS_SESSION_TOKEN = os.environ.get('IQoJb3JpZ2luX2VjEBsaCXVzLWVhc3QtMSJHMEUCIEiO9O/8lJJ90LBRn9L6cp7qxEj2wAA9Nw9YsjXE/TWkAiEAmoPxXL2koFSSuKxHcB1NGk4YLbBE7D2CZ0eLNOs3/0gqpgMIo///////////ARAAGgw1MzUwMDI4NTcxMjIiDAq69MkVyHeOu3Bs9Sr6AjPgxfWLD50VsKp2/PCs4dFgO6MzYnQYt/Ex/He2kXXchVWcA0TdQ24KLzUC/+ZAynnq+p+9Hcbv4mRejdbTBApfFhgZ/5DPf+Ye1pDNLdKreV3FbhJXPCBKwaNgEhqENCq3eMhtUx4GGsktgd/Izh2eK0eO+hAPJ8DP+wKDVU7EdDUup/4ZcYRpSDHKXRJ2n/73UiAhV1yL+dC1y0ytI7cPCn2EfqkXRwXlTityKyKtAavl+WWWIP1mUWZ2d5HKB9FznDPNBnGuDcaecDJcC7vcc65+xh7fIUbMpRlVW4kNrg7a5m3+J80tpgoSD1kznm6EIjVMK2f/1mGXyJRjbU1Lh64ag07w18uB9v94/i+HIdu/ITxJIQhxilNAmlIjx10WpHMDOwm1I0l5KcdYhpnL2CHBWVP7YzbFqNprMWrui4/9AmohHa3jYU8fUyaw2Z2t24hKEvx/sCVeaSYxZUj2xjW5vvJ9RfEbUwkgotqVkAiVFBPC4/IhxzDHrse5BjqmAVeJ2AQVoFV7P8Fpqenab/7h1e3m8v6tQSuA0wawTI1ioP7fmJ71aILFdZ5KhfpL7LJSLmwzceL/fhuhRqIA+8sCADEl0yzrXW+1/6TGaFWIlmjZ0EbzysrROIw0+x2cYz/ed1c1RTbBxXtau/lWrpxofhQWURaCXiCnZeaqE45EbASWjSQOQRtx4V1p7ARX0bkBazRTbNeeBRTwjSU+5VCXBwTEg2Q=')
# Criando a sessão do boto3
session = boto3.Session(
    aws_access_key_id='ASIAXZEFHX2RON5Y5X52',
    aws_secret_access_key='X6OBIYjYHMApAny2tMi5BbaiEfWLB474yOYEZhCU',
    aws_session_token='IQoJb3JpZ2luX2VjEBsaCXVzLWVhc3QtMSJHMEUCIEiO9O/8lJJ90LBRn9L6cp7qxEj2wAA9Nw9YsjXE/TWkAiEAmoPxXL2koFSSuKxHcB1NGk4YLbBE7D2CZ0eLNOs3/0gqpgMIo///////////ARAAGgw1MzUwMDI4NTcxMjIiDAq69MkVyHeOu3Bs9Sr6AjPgxfWLD50VsKp2/PCs4dFgO6MzYnQYt/Ex/He2kXXchVWcA0TdQ24KLzUC/+ZAynnq+p+9Hcbv4mRejdbTBApfFhgZ/5DPf+Ye1pDNLdKreV3FbhJXPCBKwaNgEhqENCq3eMhtUx4GGsktgd/Izh2eK0eO+hAPJ8DP+wKDVU7EdDUup/4ZcYRpSDHKXRJ2n/73UiAhV1yL+dC1y0ytI7cPCn2EfqkXRwXlTityKyKtAavl+WWWIP1mUWZ2d5HKB9FznDPNBnGuDcaecDJcC7vcc65+xh7fIUbMpRlVW4kNrg7a5m3+J80tpgoSD1kznm6EIjVMK2f/1mGXyJRjbU1Lh64ag07w18uB9v94/i+HIdu/ITxJIQhxilNAmlIjx10WpHMDOwm1I0l5KcdYhpnL2CHBWVP7YzbFqNprMWrui4/9AmohHa3jYU8fUyaw2Z2t24hKEvx/sCVeaSYxZUj2xjW5vvJ9RfEbUwkgotqVkAiVFBPC4/IhxzDHrse5BjqmAVeJ2AQVoFV7P8Fpqenab/7h1e3m8v6tQSuA0wawTI1ioP7fmJ71aILFdZ5KhfpL7LJSLmwzceL/fhuhRqIA+8sCADEl0yzrXW+1/6TGaFWIlmjZ0EbzysrROIw0+x2cYz/ed1c1RTbBxXtau/lWrpxofhQWURaCXiCnZeaqE45EbASWjSQOQRtx4V1p7ARX0bkBazRTbNeeBRTwjSU+5VCXBwTEg2Q='
)

s3 = session.resource('s3')

s3_client = session.client('s3')

nome_bucket = 'datalake.biancalages'

s3_client.create_bucket(Bucket=nome_bucket)

path_arq1= r"/app/series.csv"
path_arq2= r"/app/movies.csv"

nome_arq1 = r"series.csv"
nome_arq2 = r"movies.csv"

data = datetime.now().strftime("%Y/%m/%d")

path_series = f"RAW/Local/CSV/Series/{data}/{nome_arq1}"
path_moveis = f"RAW/Local/CSV/Movies/{data}/{nome_arq2}"

s3_client.upload_file(path_arq1, nome_bucket, path_series)
s3_client.upload_file(path_arq2, nome_bucket, path_moveis)

print(f'Upload do arquivo {nome_arq1} e {nome_arq2}')



