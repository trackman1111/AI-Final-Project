from gym.envs.registration import register

register(
    id='Catan-v0',
    entry_point='Catan_Env.envs:CatanPlay',
)
