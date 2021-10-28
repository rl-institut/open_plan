#!/usr/local/bin/python
python manage.py compilemessages
python manage.py makemigrations users projects dashboard && \
python manage.py migrate && \
# python manage.py loaddata 'benchmarks_fixture.json' && \
python manage.py loaddata 'multivector_fixture.json' && \
python manage.py collectstatic && \
echo 'Completed Setup Successfully!!'
