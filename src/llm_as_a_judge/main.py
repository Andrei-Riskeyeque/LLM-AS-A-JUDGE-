from openai import OpenAI
from llm_as_a_judge.attack_path_evaluator import AttackPathEvaluator
from llm_as_a_judge.config import OPENAI_API_KEY
from llm_as_a_judge.test_outputs import TEST_OUTPUTS
import datetime
import sys

def save_result_to_file(result, test_output):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"evaluation_result_{timestamp}.txt"
    
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Test Output:\n")
        file.write(test_output)
        file.write("\n\nEvaluation Result:\n")
        file.write(result)
    
    return filename

def main():
    if len(sys.argv) < 2:
        print("No test output key provided. Available keys:")
        for key in TEST_OUTPUTS.keys():
            print(f"- {key}")
        print("\nUsage: python -m src.llm_as_a_judge.main <test_output_key>")
        return

    test_output_key = sys.argv[1]
    if test_output_key not in TEST_OUTPUTS:
        print(f"Invalid test output key: {test_output_key}")
        print("Available keys:", ", ".join(TEST_OUTPUTS.keys()))
        return

    test_output = TEST_OUTPUTS[test_output_key]

    client = OpenAI(api_key=OPENAI_API_KEY)
    evaluator = AttackPathEvaluator(client)

    result = evaluator.evaluate_attack_path(test_output)
    if result:
        filename = save_result_to_file(result, test_output)
        print(f"Evaluation result saved to {filename}")
    else:
        print("Failed to generate evaluation result")

if __name__ == "__main__":
    main()