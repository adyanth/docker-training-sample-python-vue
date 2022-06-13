# Sample repository for Docker, Python, FastAPI and VueJS

## Prerequisites

Docker, of course :)
Prefer either docker-ce on linux or Docker Desktop on other platforms

## Building container images

```bash
# A simple HTML based UI with single stage Dockerfile
docker build -t sample-app:simpleui .

# A Vue app with multistage Dockerfile
docker build -t sample-app:fancyui -f Dockerfile.multistage .
```

## Running containers

```bash
# A simple HTML based UI with single stage Dockerfile
docker run -p 8080:8080 sample-app:simpleui

# A Vue app with multistage Dockerfile
docker run -p 8080:8080 sample-app:fancyui
```

Open [http://127.0.0.1:8080](http://127.0.0.1:8080) to see your application in action!
