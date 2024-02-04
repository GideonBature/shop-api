# SHOP RESTful API

## Create Shop

### Create Products

### Create an image

docker build -t shop-api

### Run the container
docker run -d -p 5000:5000 -w /app -v "$(pwd):/app" shop-api

-w -> Current working directory of the container
-v -> Linking the pwd(host) to work directory of the container
