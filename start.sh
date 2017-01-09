celery worker -A multi_server_workers -Q default --loglevel=DEBUG --without-gossip --without-mingle --without-heartbeat -Ofair -c 4
