FROM postgres:16-alpine

# Database config – use these in docker-compose and backend
ENV POSTGRES_USER="postgres"
ENV POSTGRES_PASSWORD="ahmad1807"
ENV POSTGRES_DB="recipesdb"

# Copy init.sql so Postgres runs it automatically on first start
COPY init.sql /docker-entrypoint-initdb.d/
