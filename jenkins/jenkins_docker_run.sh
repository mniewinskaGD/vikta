docker run \
  -p 8080:8080 \
  -p 50000:50000 \
  -d --name jenkins-docker \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v jenkins_home:/var/jenkins_home \
  --group-add 103 \
  my-jenkins-python
