#!/usr/bin/env python3

import connexion


def solve(jobs):
    return jobs


app = connexion.App(__name__)
app.add_api('swagger.yaml')
# set the WSGI application callable to allow using uWSGI:
# uwsgi --http :8080 -w app -p 16
application = app.app

if __name__ == '__main__':
    app.run(port=8080, server='gevent')
