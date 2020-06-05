FROM jupyterhub/k8s-hub:0.8.2

ADD mck_init ./mck_init/

USER root

RUN pip3 install mck_init/

USER jovyan

