UNAME="fckuligowski"
UPASS='Tigerbomb$01'
REPO="fckuligowski/abagdemo"
TAG="v1.1.104"
TOKEN=$(curl -s -H "Content-Type: application/json" -X POST -d '{"username": "'${UNAME}'", "password": "'${UPASS}'"}' https://hub.docker.com/v2/users/login/ | jq -r .token)
EXISTS=$(curl -s -H "Authorization: JWT ${TOKEN}" https://hub.docker.com/v2/repositories/$REPO/tags/?page_size=10000 | jq -r "[.results | .[] | .name == \"$TAG\"] | any")
#curl -s -H "Authorization: JWT ${TOKEN}" https://hub.docker.com/v2/repositories/$REPO/tags/?page_size=10000
echo $EXISTS