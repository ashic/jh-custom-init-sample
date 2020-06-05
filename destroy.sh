# Suggested values: advanced users of Kubernetes and Helm should feel
# free to use different values.
RELEASE=jhub
NAMESPACE=jhub

helm delete $RELEASE -n $NAMESPACE
