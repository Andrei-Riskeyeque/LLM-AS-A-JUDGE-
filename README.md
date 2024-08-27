# LLM as Judge

This project uses OpenAI's GPT model to evaluate attack paths outputs.


## Project Details

- **Name**: LLM as Judge
- **Version**: 0.1.0
- **Author**: Andrei Moise (neuronspeeed@gmail.com)
- **Description**: LLM as a judge for evaluating attack paths
- **License**: MIT



## Setup

1. Ensure you have Python 3.8 or higher installed.

2. Clone this repository and navigate to the project directory:
   ```
   git clone https://github.com/your-username/LLM-AS-A-JUDGE.git
   cd LLM-AS-A-JUDGE
   ```

3. Create a virtual environment and activate it:
   ```
   python -m venv .venv
   .venv\Scripts\Activate.ps1  # On Windows PowerShell
   # OR
   source .venv/bin/activate  # On Unix or MacOS
   ```

4. Install the required packages:
   ```
   pip install python-dotenv openai "langchain<0.1.0" "langchain-openai<0.1.0"
   ```

5. Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_KEY=your_openai_api_key_here
   ```

## Usage

Run the script with:

```
python main.py <test_output_key>
```

Available test output keys: example1, example2

Example:

```
python main.py example1
rye run python -m src.llm_as_a_judge.main example1
```


This will evaluate the specified test output and save the result to a text file.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.


