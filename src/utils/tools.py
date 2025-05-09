import random
import dotenv

def random_number(min_value:float, max_value:float) -> float:
    return random.uniform(min_value, max_value)

def is_multiple(number_target:int, number_base:int) -> bool:
    return number_target % number_base == 0

def load_env(dotenv_path:str) -> dict:
    return dotenv.dotenv_values(dotenv_path)


