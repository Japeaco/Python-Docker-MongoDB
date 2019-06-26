import docker
from docker import types

client = docker.from_env()

client.swarm.init(
  listen_addr='0.0.0.0:8080', force_new_cluster=False
)

client.networks.create(name="net", driver="overlay", scope="swarm")

client.images.pull('nclcloudcomputing/javabenchmarkapp:latest')
client.images.pull('mongo:latest')
client.images.pull('dockersamples/visualizer:latest')

javaPorts = docker.types.EndpointSpec(ports={80: (8080, "tcp")})
mongoPorts = docker.types.EndpointSpec(ports={3306: (27017, "tcp")})
visPorts = docker.types.EndpointSpec(ports={88: (8080, "tcp")})

javareplicas = docker.types.ServiceMode('replicated', replicas=2)
replicas = docker.types.ServiceMode('replicated', replicas=1)

client.services.create(image='nclcloudcomputing/javabenchmarkapp', mode=javareplicas,
                       name='javaimages', networks=["net"], endpoint_spec=javaPorts)
client.services.create(image='mongo', name='mongodb', mode=replicas,
                       networks=["net"], endpoint_spec=mongoPorts)
client.services.create(image='dockersamples/visualizer', mode=replicas, name='visualizer',
                       networks=["net"], endpoint_spec=visPorts,
                       mounts=["/var/run/docker.sock:/var/run/docker.sock"])