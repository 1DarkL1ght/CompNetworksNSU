docker network create parser_network

docker build -t api ./api
docker build -t db ./db
docker build -t nginx ./nginx

docker run -d --name api_container --network parser_network -p 8080:8080 api
docker run -d --name db_container --network parser_network -p 5432:5432 db
docker run -d --name nginx_container --network parser_network -p 80:80 nginx