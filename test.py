from flask import Flask
import datetime
from flask_apscheduler  import APScheduler
app = Flask(__name__)
aps = APScheduler()


@app.route("/")
def index():
    return "<h2 style='color:red'>Hello World</h2>"


class Config(object):
    JOBS = [
        {
            'id': 'job1',
            'func': 'test:task',
            'args': (1, 2),
            'trigger': 'interval',
            'seconds': 10
        }
    ]
    SCHEDULER_API_ENABLED = True


def task(a, b):
    print(str(datetime.datetime.now()) + ' execute task ' + '{}+{}={}'.format(a, b, a + b))


if __name__ == '__main__':
    app = Flask(__name__)
    app.config.from_object(Config())

    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    app.run()
    # app.run(port=8000)

# if __name__ == "__main__":
#     app.run()