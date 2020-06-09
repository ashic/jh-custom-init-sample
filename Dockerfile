FROM jupyterhub/k8s-hub:0.9-17c3f1d

ADD mck_init ./mck_init/

USER root

RUN pip3 install mck_init/

USER jovyan

