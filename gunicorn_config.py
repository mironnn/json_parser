#web: gunicorn my_json.wsgi --log-file -
command = '/home/my_chart/bin/gunicorn'
pythonpath = '/home/my_chart/bin/src/'
bind = '127.0.0.1:8001'
#bind = '95.85.1.143:8001'
workers = 3
#user = nobody
