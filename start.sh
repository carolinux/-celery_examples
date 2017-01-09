celery worker -A multi_server_workers -Q celery --loglevel=DEBUG --without-gossip --without-mingle --without-heartbeat -Ofair -c 4
