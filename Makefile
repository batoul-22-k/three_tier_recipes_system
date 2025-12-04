# Namespace for the app
NAMESPACE=recipes-app

# Deploy all Kubernetes resources
k8s-deploy:
	kubectl create namespace $(NAMESPACE) --dry-run=client -o yaml | kubectl apply -f -
	kubectl apply -n $(NAMESPACE) -f k8s/recipes-app.yaml


# Show status of all resources
k8s-status:
	kubectl get all -n $(NAMESPACE)

# Open frontend using minikube
k8s-open:
	minikube service recipes-frontend -n $(NAMESPACE)

# Remove everything
k8s-clean:
	kubectl delete namespace $(NAMESPACE)
