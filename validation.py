import json
from typing import Optional

from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser


validation_config = {
    "completeness_check_questions": "Do all the subsections have the complete information and provide detailed explanations for each identified point?",
    "toxicity_check_questions": "Do the subsection include any language that could be considered offensive, harmful,inappropriate,any form of hate speech or cyberbullying?",
    "factual_accuracy_check_questions": [
        "Are all the sentences (or facts) in the tool response derived exclusively from the provided tool context?",
        "Is there any additional information that is not present in the tool context included in the tool response?",
        "Does the tool response introduce any facts or details that cannot be directly traced back to the tool context?",
        "Are all of the identified facts, numbers, and nouns in the tool response present in the tool context?",
        "Are there any discrepancies in the numerical data between the tool context and the tool response?",
    ],
    "validation_prompt_json_string": json.dumps(
        [
            (
                "system",
                """
                    You are an assistant who evaluates the correctness of a tool response.Validate the given tool response against the
                    validation Criteria and return the result in JSON format.

                    Validation Criteria
                    >>>
                    {validation_criteria}
                    <<<

                    Relevancy Check 
                    >>>
                    {relevance_check_questions}
                    <<<

                    Factual Accuracy Check 
                    >>>
                    {factual_accuracy_check_questions}
                    <<<

                    Completeness Check 
                    >>>
                    {completeness_check_questions}
                    <<<

                    Toxicity Check
                    >>>
                    {toxicity_check_questions}
                    <<<

                    Tool Response
                    >>>
                    {tool_response}
                    <<<

                    Tool Context
                    >>>
                    {tool_context}
                    <<<

                    Format Instructions
                    >>>
                    {format_instructions}
                    <<<

                    Instructions:
                    1. For the given validation criteria, there are subsection-wise criteria questions provided. Therefore, validate the tool's response against only the provided validation criteria.
                    2. Provide your feedback if the subsection data answers every question in subsection wise criteria questions related to that particular subsection and then provide outcome as "1" or "0" based on your feedback.
                    3. Outcome should be "0" or "1" for every question in subsection wise criteria questions.
                    4. Outcome should be "1" to a question only if all the points in the subsection are relevant to the question.Outcome should be "0" to the question if even one point is not relevant to the question.
                    5. Provide every question in subsection wise criteria questions for every point in the tool response.
                    6. If there is no data in any of the subsection, do not validate that subsection and assign the subsection to null.
                    7. If there are no questions provided for any of the validation criteria,assign that validation criteria to null.
                    8. If there is no information in any of the subsection in the data, then assign null to the feedback and outcome.
                    9. Response should always start with the subsections mentioned in format instructions as keys, without any additional keys or introductory text and should always include all the criterion.
                    10. Provide the response following format instructions.

                """,
            ),
            (
                "user",
                "Please provide the criteria feedback and outcome based on feedback",
            ),
        ]
    ),
}

def validate_tool_response(
    tool_specific_pydantic_parser: PydanticOutputParser,  
    tool_response: str,  
    tool_context: Optional[str] = "",
    is_factual_response: bool = True,
    relevance_questions: Optional[str] = "", 

):
    """
    Validate the tool response across multiple validation criteria
    """
    validation_criteria = ["Completeness","Toxicity"]
    validation_criteria = validation_criteria.append("Factual Accuracy") if is_factual_response else validation_criteria.append("Relevance")
    factual_accuracy_check_questions = validation_config["factual_accuracy_check_questions"] if is_factual_response else ""
    messages_template = [
        tuple(li) for li in json.loads(validation_config["validation_prompt_json_string"])
    ]
    chat_template = ChatPromptTemplate.from_messages(messages_template)
    format_instructions = tool_specific_pydantic_parser.get_format_instructions()
    chain = (
        chat_template
        | ChatOpenAI(model="gpt-4o", temperature=0)
        | tool_specific_pydantic_parser
    )
    return chain.invoke(
        {
            "validation_criteria": validation_criteria,
            "relevance_check_questions": relevance_questions,
            "factual_accuracy_check_questions": factual_accuracy_check_questions,
            "completeness_check_questions": validation_config["completeness_check_questions"],
            "toxicity_check_questions": validation_config["toxicity_check_questions"],
            "tool_response": tool_response,
            "tool_context": tool_context,
            "format_instructions": format_instructions,
        }
    )
