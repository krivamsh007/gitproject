# Create directory structure
mkdir -p {dags,notebooks,init,delta_storage/{raw,processed,curated}}

# Build and start
docker-compose build
docker-compose up -d

# Initialize Superset
docker-compose exec superset superset fab create-admin \
  --username admin \
  --firstname Admin \
  --lastname User \
  --email admin@example.com \
  --password admin
docker-compose exec superset superset db upgrade
docker-compose exec superset superset initadmin