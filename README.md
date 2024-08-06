# atoz_poc


Jenkins :
for jenkins we used officail documentation for installation

Argocd:
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl get pods -n argocd
kubectl apply -f volume.yml
kubectl edit deployment argocd-server -n argocd
In the spec.template.spec.containers section, add the volume mount:
volumeMounts:
  - name: argocd-storage
    mountPath: /data  # This path should match the path used in ArgoCD for persistent storage

In the spec.template.spec section, add the volume:
volumes:
  - name: argocd-storage
    persistentVolumeClaim:
      claimName: argocd-pvc

kubectl apply -f ingress.yml

Get Initial Admin Password:
The default username is admin. Retrieve the initial password with the following command:

kubectl get secret argocd-initial-admin-secret -n argocd -o jsonpath="{.data.password}" | base64 --decode

