pip install virtualenv
virtualenv env
source env/bin/activate
echo "source env/bin/activate"
pip install -r requirements.txt

python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate

