Clone the version-10 branch of this repo

```shell
git clone https://github.com/flexlar/flexlar_docker.git -b version-10 && cd flexlar_docker
```

Build the images

```shell
export DOCKER_REGISTRY_PREFIX=flexlar
docker build -t ${DOCKER_REGISTRY_PREFIX}/flexlar-socketio:v10 -f build/flexlar-socketio/Dockerfile .
docker build -t ${DOCKER_REGISTRY_PREFIX}/flexlar-nginx:v10 -f build/flexlar-nginx/Dockerfile .
docker build -t ${DOCKER_REGISTRY_PREFIX}/erpnext-nginx:v10 -f build/erpnext-nginx/Dockerfile .
docker build -t ${DOCKER_REGISTRY_PREFIX}/flexlar-worker:v10 -f build/flexlar-worker/Dockerfile .
docker build -t ${DOCKER_REGISTRY_PREFIX}/erpnext-worker:v10 -f build/erpnext-worker/Dockerfile .
```
