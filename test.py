from dotenv import load_dotenv, find_dotenv, dotenv_values
import os

config = {
    **dotenv_values(".env.test"),  # load shared development variables
}

print(config.get(list))