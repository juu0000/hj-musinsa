# hj-musinsa

### Build
```
$cd iam-api
docker buildx build \
--platform linux/amd64,linux/arm64,linux/arm/v7 \
--build-arg AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} --build-arg AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY} \
-t docconman/iam-api:latest \
--push .
```

### Run
* Docker
```
$docker run -p 127.0.0.1:5000:5000 
```

* Kubernetes
```
$cd manifest
$kubectl apply -f .
```

### Usage
```
GET http://localhost:5000/old-iam?hours=${time}
```