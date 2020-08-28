# Create a Service Account that will be allowed to deploy 
# priviliged containers.
kubectl create serviceaccount -n abagdemo abagdemo-priv
# Bind that SA to the ClusterRole that Tanzu Mission Control
# provides for privileged containers (vmware-system-tmc-psp-privileged).
# That clusterrole is bound to the Pod Security Policy that
# allows privileged containers (vmware-system-tmc-privileged).
# (It was just easier to use VMware's PSP rather than go thru the
# hassle of creating my own).
kubectl create clusterrolebinding abagdemo-priv-binding \
--clusterrole=vmware-system-tmc-psp-privileged \
--serviceaccount=abagdemo:abagdemo-priv
