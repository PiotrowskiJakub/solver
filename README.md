## Solver

API for solver implemented with [Connexion](https://github.com/zalando/connexion) framework and supporting [Swagger](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md) specification.

### Running Locally
You can run the application directly on your local operating system:
```bash
$ pip3 install -r requirements.txt
$ ./app.py
```
### Running with Docker
You can build the application as a Docker image and run it:
```bash
$ docker build -t solver .
$ docker run -d -p 8080:8080 solver
```

Documentation is available under [/ui](http://localhost:8080/ui/)