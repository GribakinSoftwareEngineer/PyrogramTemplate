import environs

env = environs.Env()
env.read_env()

API_ID = env.str("API_ID")
API_HASH = env.str("API_HASH")
SESSION_NAME = env.str("SESSION_NAME")
