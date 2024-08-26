from openai import OpenAI
from llm_as_a_judge.prompt_template import EVALUATION_PROMPT_TEMPLATE
from llm_as_a_judge.config import DEFAULT_MODEL
class AttackPathEvaluator:
    def __init__(self, client):
        self.client = client

    def generate_evaluation_prompt(self, test_output):
        return EVALUATION_PROMPT_TEMPLATE.format(attack_path=test_output)

    def evaluate_attack_path(self, test_output, model=DEFAULT_MODEL):
        prompt = self.generate_evaluation_prompt(test_output)
        
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are an expert assistant who evaluates the correctness of an attack path. Provide a detailed evaluation in plain text."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0,
                max_tokens=1000
            )

            return response.choices[0].message.content
        except Exception as e:
            print(f"An error occurred: {e}")
            return None