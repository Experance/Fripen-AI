import os
from multiprocessing import cpu_count


bind = 'unix:/app/gunicorn.sock'
preload_app = True
# worker_class = 'uvicorn.workers.UvicornWorker' # if your app supports ASGI (Flask does not), uncomment this to use ASGI/uvicorn workers
workers = int(os.environ.get('WORKERS', cpu_count() * 8 + 1))
timeout = int(os.environ.get('TIMEOUT', 120))
access_log_format = '%(h)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" "%({X-Forwarded-For}i)s" "%({X-Forwarded-Port}i)s" "%({X-Forwarded-Proto}i)s"  "%({X-Amzn-Trace-Id}i)s"'
max_requests = int(os.environ.get('MAX_REQUESTS', 16384))
limit_request_line = int(os.environ.get('LIMIT_REQUEST_LINE', 8190))
keepalive = int(os.environ.get('KEEPALIVE', 60))