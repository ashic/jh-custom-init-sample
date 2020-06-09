from z2jh import get_config, set_config_if_not_none

def get_secret(key):
    if key == "client_secret":
        return "super_duper"
    elif key == "login_service":
        return "bouncy bouncy"
    elif key == "cookie_secret":
        return "40671ad8c01fb14fc59f589995487882bcd459339a808ff0380a7897576e70b6"
    elif key == "proxy_secret":
        return "e64a6dc7dfb3b3dac7f6a3b52429d92d2f5b17bb311625b2617e89eda62ed15b"
    elif key == "jup_client_id":
        return "e54b8b9e-868b-440f-9e85-8b86b0e51a12"
    else:
        raise Exception(f"Unsupported key: {key}")


def get_value(current):
    if current and isinstance(current, str) and current.startswith("mck://"):
        secret_key = current[6:]
        secret_value = get_secret(secret_key)

        return secret_value
    
    return current

def init_mck_secrets(c):
    auth_type = get_config('auth.type')

    if auth_type == "custom":
        full_class_name = get_config('auth.custom.className')
        c.JupyterHub.authenticator_class = full_class_name
        auth_class_name = full_class_name.rsplit('.', 1)[-1]
        auth_config = c[auth_class_name]

        current_config = get_config('auth.custom.config' or {})

        new_config = {k:get_value(current_config[k]) for k in current_config}
        auth_config.update(new_config)

    # cookie secret
    c.JupyterHub.cookie_secret = get_value(get_config("custom.hub_cookie_secret")).encode()

    # proxy token
    # the proxy secret can't be "read in " using get_config(). 
    # setting the auth token like this will break things unless the
    # the proxy pod is also using the same auth token. 
    # c.ConfigurableHTTPProxy.auth_token = get_value("mck://proxy_secret")


    # jup client id
    # c.KubeSpawner.environment
    singleUserEnv = get_config("singleuser.extraEnv" or {})
    c.KubeSpawner.environment = {k:get_value(singleUserEnv[k]) for k in singleUserEnv}
