# AI Agent (Boot.dev Project)

A simple AI Agent built in Python that uses function calling to interact with tools such as listing files, reading/writing, and executing Python scripts.  
This project was completed as part of the Boot.dev backend development course.

---

## Features
- Feedback loop for iterative reasoning  
- Tools for:  
  - Listing files and directories  
  - Reading file contents  
  - Writing/overwriting files  
  - Executing Python files  
- Example calculator app with unit tests  

---

## Requirements
- Python 3.12+  
- [uv](https://docs.astral.sh/uv/) or pip for dependency management  
- (Optional) A virtual environment  

---

## How to Run

```bash
# Install dependencies
uv sync
# or
pip install -r requirements.txt

# Clone this repository
git clone https://github.com/YOUR_USERNAME/ai-agent.git
cd ai-agent

# Run the agent
uv run main.py "Fix the bug in the calculator"

# Run tests
uv run tests.py


aiAgent/
├── calculator/          # Example calculator project
├── functions/           # Tool functions
├── pkg/                 # Core logic
├── tests.py             # Unit tests
├── main.py              # Entry point
├── README.md            # Documentation
└── pyproject.toml       # Dependencies & config
