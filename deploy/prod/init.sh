APP_NAME="portfoliov2"

sudo -u postgres psql -f init_db.sql # Init database
sudo docker run -it eu.gcr.io/goodbarber-service-plus/$APP_NAME:latest sh -c "python manage.py migrate"
