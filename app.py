#!/usr/bin/env python3

import connexion

from genetic import genetic


def solve(jobs):
    times_list = list(map(lambda job: job['times'], jobs['jobs']))
    return genetic(times_list)


app = connexion.App(__name__)
app.add_api('swagger.yaml')
# set the WSGI application callable to allow using uWSGI:
# uwsgi --http :8080 -w app -p 16
application = app.app

if __name__ == '__main__':
    app.run(port=8080, server='gevent')
