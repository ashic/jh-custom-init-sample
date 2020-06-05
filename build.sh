#ensure we're in minikube
eval $(minikube -p minikube docker-env)

docker build -t jhfoo:0.8.2 .
