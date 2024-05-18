
DEFAULT_TEMPLATE = """<bos><start_of_turn>system
You are an English to French translation AI. Given some **text**, you will translate the whole text directly to French. You must only provide the translation in your output, no other words are to be spoken.<end_of_turn>
<start_of_turn>text
Text to translate: "{text}"<end_of_turn>
<start_of_turn>translation
"""

class PromptTemplate:

    def __init__(
            self,
            prompt_template: str = DEFAULT_TEMPLATE
    ):
        self.prompt_template = prompt_template

    def get_prompt(
            self, 
            text:str
    )->str:
        return self.prompt_template.format(text=text)
