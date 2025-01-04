import json
import boto3
import requests
import os
from datetime import datetime

# Configurações da API TMDb
API_KEY = os.getenv("TMDB_KEY")
BASE_URL = "https://api.themoviedb.org/3"
GENRE_NAMES = ["Drama", "Romance"]
MIN_RATING = 5.0
DECADES = [1980, 1990, 2000, 2010]

# Configurações do AWS S3
S3_BUCKET = "datalake.biancalages"
S3_PREFIX = "RAW/TMDB"

# Função para buscar o ID dos gêneros Romance e Drama
def get_genre_ids():
    url = f"{BASE_URL}/genre/movie/list"
    params = {
        "api_key": API_KEY,
        "language": "en-US"
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"Erro na requisição de gêneros: {response.json()}")
        return []

    genres = response.json().get("genres", [])
    genre_ids = [genre["id"] for genre in genres if genre["name"] in GENRE_NAMES]
    return genre_ids

# Função para buscar filmes por década com nota >= 5.0.
def fetch_movies_by_decade(decade, max_results=100):
    genre_ids = get_genre_ids()
    if not genre_ids:
        return []

    movies = []
    start_year = decade
    end_year = start_year + 9
    page = 1

    while len(movies) < max_results:
        url = f"{BASE_URL}/discover/movie"
        params = {
            "api_key": API_KEY,
            "with_genres": ",".join(map(str, genre_ids)),
            "primary_release_date.gte": f"{start_year}-01-01",
            "primary_release_date.lte": f"{end_year}-12-31",
            "vote_average.gte": MIN_RATING,
            "page": page,
        }
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print(f"Erro na requisição para década {decade}: {response.json()}")
            break

        data = response.json()
        results = data.get("results", [])
        movies.extend(results)
        page += 1
        if page > data["total_pages"]:
            break

        if len(movies) >= max_results:
            break

    # Obtem detalhes adicionais de cada filme, incluindo orçamento
    detailed_movies = []
    for movie in movies[:max_results]:
        movie_id = movie["id"]
        detail_url = f"{BASE_URL}/movie/{movie_id}"
        detail_params = {
            "api_key": API_KEY,
            "language": "en-US"
        }
        detail_response = requests.get(detail_url, params=detail_params)
        if detail_response.status_code == 200:
            detailed_movies.append(detail_response.json())
        else:
            detailed_movies.append(movie)  # Adiciona dados básicos se a requisição detalhada falhar

    return detailed_movies

# Função para salvar JSON no S3
def upload_to_s3(data, filename):
    """Faz upload de um arquivo JSON para o bucket S3."""
    s3_client = boto3.client('s3')
    date_str = datetime.now().strftime("%Y/%m/%d")
    s3_key = f"{S3_PREFIX}/{date_str}/{filename}"

    # Converte os dados para JSON
    json_data = json.dumps(data, ensure_ascii=False, indent=4)
    try:
        s3_client.put_object(
            Bucket=S3_BUCKET,
            Key=s3_key,
            Body=json_data,
            ContentType="application/json"
        )
        print(f"Arquivo enviado para o S3: {s3_key}")
    except Exception as e:
        print(f"Erro ao enviar {filename} para o S3: {str(e)}")

# Função principal para AWS Lambda
def lambda_handler(event, context):
    """Função principal para rodar no AWS Lambda."""
    for decade in DECADES:
        movies = fetch_movies_by_decade(decade)
        filename = f"romance_drama_{decade}s.json"
        upload_to_s3(movies, filename)

    return {
        "statusCode": 200,
        "body": json.dumps("Arquivos processados e enviados para o S3!")
    }


