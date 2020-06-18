# Suggested values: advanced users of Kubernetes and Helm should feel
# free to use different values.
RELEASE=jhub
NAMESPACE=jhub

helm upgrade --install $RELEASE jupyterhub/jupyterhub \
  --namespace $NAMESPACE  \
  --version=0.8.2 \
  --values config.yaml

kubectl patch deploy -n $NAMESPACE hub --type json --patch '[{"op": "replace", "path": "/spec/template/spec/containers/0/command", "value": ["bash", "-c", "\nmkdir -p ~/hotfix\ncp -r /usr/local/lib/python3.6/dist-packages/kubespawner ~/hotfix\nls -R ~/hotfix\npatch ~/hotfix/kubespawner/spawner.py << EOT\n72c72\n<             key=lambda x: x.last_timestamp,\n---\n>             key=lambda x: x.last_timestamp and x.last_timestamp.timestamp() or 0.,\nEOT\n\nPYTHONPATH=$HOME/hotfix jupyterhub --config /srv/jupyterhub_config.py --upgrade-db\n"]}]'
