from typing import Tuple

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

from src.prompts import PromptTemplate
from src.configs import ModelConfigs


class Model:

    def __init__(
        self,
        prompt_template:PromptTemplate,
        model_configs:ModelConfigs,
    ):
        self.model_configs = model_configs
        self.prompt_template = prompt_template
        self.device = self._set_device()
        self.model, self.tokenizer = self._load_model(
            self.model_configs.MODEL_NAME.value
        )

    def _set_device(self)->str:
        return (
            "cuda" if torch.cuda.is_available() else 
            "mps" if torch.backends.mps.is_available() else 
            "cpu"
        )
    
    def _load_model(
            self, 
            model_name:str
    )->Tuple[AutoModelForCausalLM, AutoTokenizer]:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        model.to(self.device)
        return model, tokenizer
    

    def generate(
            self,
            text:str
    )->str:
        prompt = self.prompt_template.get_prompt(text=text)
        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids.to(self.device)
        input_len = input_ids.shape[1]

        output = self.model.generate(
            input_ids, 
            max_length=self.model_configs.MAX_LENGTH.value,
            temperature=self.model_configs.TEMPERATURE.value,
        )[0]

        return self.tokenizer.decode(
            output[input_len:], 
            skip_special_tokens=True
        )