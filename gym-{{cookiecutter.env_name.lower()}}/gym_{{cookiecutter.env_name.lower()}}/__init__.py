from gym.envs.registration import register

register(
    id='{{cookiecutter.env_name}}-v0',
    entry_point='gym_{{cookiecutter.env_name.lower()}}.envs:{{cookiecutter.env_name}}Env',
)
