import docker

client = docker.from_env()

client.images.pull('nclcloudcomputing/javabenchmarkapp:latest')
client.containers.run('nclcloudcomputing/javabenchmarkapp', ports={'8080/tcp': 80})
