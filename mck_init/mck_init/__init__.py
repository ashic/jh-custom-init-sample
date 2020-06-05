from z2jh import get_config, set_config_if_not_none

def get_secret(key):
    if key == "client_secret":
        return "super_duper"
    elif key == "login_service":
        return "bouncy bouncy"
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
