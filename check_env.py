from environ import Env
from pathlib import Path

# Inicializa las variables de entorno
env = Env()

# Define la ruta del archivo .env
env_path = Path(__file__).resolve().parent / 'core' / '.env'

# Lee el archivo .env desde la ruta correcta
Env.read_env(env_path)

# Imprime los valores de las variables de entorno
print("Database name:", env('DATABASE_NAME', default="Not Found"))
print("Database user:", env('DATABASE_USER', default="Not Found"))
print("Database password:", env('DATABASE_PASSWORD', default="Not Found"))
