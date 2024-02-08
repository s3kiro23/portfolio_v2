source /opt/portfoliov2/config.ini

APP_NAME="portfoliov2"

sudo -u postgres psql -f init_db.sql # Init database
sudo docker run -it $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$APP_NAME:latest sh -c "python manage.py migrate"
