from enum import Enum


class ModelConfigs(Enum):

    MODEL_NAME:str = "gemma-2b-translate"
    TEMPERATURE:float = 0.7
    MAX_LENGTH:int = 100