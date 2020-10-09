CERTDIR=/home/ubuntu/tanzu/certs/nginx
kubectl create secret generic abagdemo-nginx-sslcert \
--from-file=$CERTDIR/nginx.crt --from-file=$CERTDIR/nginx.key -n abagdemo \
--dry-run -o yaml | kubectl apply -f -
