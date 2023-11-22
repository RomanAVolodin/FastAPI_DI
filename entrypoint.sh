if [ "$POSTGRES_DB" = "auth" ]
then
    echo "Waiting for postgres..."
    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done
    echo "PostgreSQL started"
fi


NUM_WORKERS=3
TIMEOUT=120

python main.py