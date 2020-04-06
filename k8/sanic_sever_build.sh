docker build -t navalta3030/sanic-server -f ./../Dockerfile ./../

docker push navalta3030/sanic-server:latest

kubectl apply -f .