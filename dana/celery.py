import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dana.settings')

app = Celery(
    main='dana',
    broker='amqp://',
    backend='rpc://',
    include=['dana.tasks'],
)

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
