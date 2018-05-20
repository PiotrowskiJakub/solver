#!/usr/bin/env python3

import connexion

from genetic import genetic


def solve(jobs):
    times_list = list(map(lambda job: job['times'], jobs['jobs']))
    scheduled_times = genetic(times_list)
    scheduled_jobs = [jobs['jobs'][i - 1] for i in scheduled_times]
    return {'jobs': scheduled_jobs}


app = connexion.App(__name__)
app.add_api('swagger.yaml')
# set the WSGI application callable to allow using uWSGI:
# uwsgi --http :8080 -w app -p 16
application = app.app

if __name__ == '__main__':
    app.run(port=8080, server='gevent')
