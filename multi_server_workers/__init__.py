from celery import Celery


celeryapp = Celery('tasks')
celeryapp.config_from_object('multi_server_workers.celery_config')

