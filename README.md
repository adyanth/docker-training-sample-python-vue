# Sample repository for Docker, Python, FastAPI and VueJS

## Prerequisites

Docker, of course :)
Prefer either docker-ce on linux or Docker Desktop on other platforms
Install `docker-compose`, or use the latest `docker compose` commands

## Building container images

Build the container images from the Dockerfile using the below commands.

```bash
# A simple HTML based UI with single stage Dockerfile
docker build -t sample-app:simpleui .

# A Vue app with multistage Dockerfile
docker build -t sample-app:fancyui -f Dockerfile.multistage .
```

## Running containers

To run the containers from the images built above, see below.

```bash
# A simple HTML based UI with single stage Dockerfile
docker run -p 8080:8080 sample-app:simpleui

# A Vue app with multistage Dockerfile
docker run -p 8080:8080 sample-app:fancyui
```

Open [http://127.0.0.1:8080](http://127.0.0.1:8080) to see your application in action!

## Orchestrating with docker compose

Using docker compose, we can spin up multiple related applications with just one command.

```bash
# New v2 syntax
docker compose up -d
# Old docker-compose binary
docker-compose up -d
```

Then, proceed to visit [http://127.0.0.1:8080](http://127.0.0.1:8080), [http://127.0.0.1:8081](http://127.0.0.1:8081), [http://127.0.0.1:8082](http://127.0.0.1:8082) and [http://127.0.0.1:8083](http://127.0.0.1:8083) to see different behaviours.
