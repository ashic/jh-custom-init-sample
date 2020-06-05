# jh-custom-init-sample
Sample demonstrating custom jupyterhub config initialisation with value lookup


## prerequisites

* minikube must be running
* must have a namespace called jhub

## steps

build the container:

```
./build.sh
```

deploy jupyterhub:

```
./setup.sh
```

when done:

```
./destroy.sh
```

# Notes

In this sample, we create a docker image based off the jupyterhub/k8s-hub image. We add a python module called mck_init which rewrites required settings. We call out to the module from the config.yaml passed to the jupyterhub helm chart. 

## Points of interest in config.yaml

#### image

This is the one we built. 

#### extraConfig

Custom bit of initialisation python. We're calling out to our mck_init module. 

#### login_service / client_secret

This is demonstrating value substitution. Configs in this section that start with mck:// will use the value without "mck://" to look up the actual value to use. In the mck_init module, this is done via the get_secret() function. In practice this can be used to look up secrets from external sources. Values that don't start with mck:// are left untouched. 

In the sample code, a value that is not a string is ignored (e.g. userdata_params). 







