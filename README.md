# AI Design — Building Large-Scale AI Systems

Welcome to the AI Design course from the **University of Trento (2026)**.

This repository contains course materials, labs, and project directions for designing and building AI-powered systems where Large Language Models (LLMs) act as core components—making decisions, using tools, and managing state—rather than being simple text generators.

## 📚 Course Overview

The course is organized around five practical learning modules followed by a culminating evaluation session:

### Labs

1. **[Lab 01: Hello World](labs/01_hello_world/)** — Foundation concepts and getting started
   - Basic chat interactions
   - Streaming responses
   - Voice I/O with LLMs
   - Image processing basics

2. **[Lab 02: Standalone Agents](labs/02_standalone_agents/)** — Building autonomous agents
   - Stateless agents
   - Stateful agents  
   - Short-term memory (session-based)
   - Long-term memory and persistence
   - Single-call vs. multi-turn agents
   - Testing and metrics for agent behavior

3. **[Lab 03: AI API & Integration](labs/03_ai-api/)** — System design patterns
   - Agentic loops and autonomy
   - Tool calling and MCP (Model Context Protocol)
   - State and context management
   - Safety guardrails and observability
   - Architecture of AI systems (AOA framework)
   - Logging and observability in practice

4. **[Lab 04: Evaluation](labs/04_eval/)** — Measuring system quality
   - Testing strategies
   - Designing meaningful evaluations
   - "Optimizing in the Dark" framework
   - Cost-benefit analysis

5. **[Lab 10: Evaluation Session](labs/10_lab_eval_session/)** — Capstone evaluation workshop
   - Model comparison guidelines
   - Practical evaluation exercises

## 🎯 Course Projects

Students choose one of three project tracks that emphasize the three pillars: **design alternatives**, **honest experiments**, and **clear communication**.

### Project 1: AI-Powered Course Hub
A knowledge management platform where students and professors collaboratively organize course materials, ask/answer questions, and AI assists with auto-answers, catch-up summaries, and assignment pre-checks.

**Key challenges**: Answer quality and knowing when to defer to humans; relevance ranking across heterogeneous content; evaluating human vs. AI contributions.

### Project 2: Social Network for Agents (and Humans)
A social platform where AI agents replicate human personas and interact with each other, exploring emergent multi-agent dynamics.

**Key challenges**: Persona consistency; meaningful (not trivial) interactions; measuring social dynamics quantitatively.

### Project 3: Conversational Clustering
An AI agent that iteratively clusters data through dialogue with a human, learning to ask good questions and reconcile contradictory feedback.

**Key challenges**: Handling conflicting guidance; evaluating clustering quality without ground truth; knowing what to ask and when.

See [AI_Design_Projects_2026.md](AI_Design_Projects_2026.md) for detailed descriptions, design considerations, and evaluation frameworks.

## 🚀 Getting Started

### Prerequisites
- Python 3.12+
- pip or conda for package management
- An OpenAI API key (or compatible LLM provider)

### Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd ai-design-2026-pub
```

2. Install dependencies:
```bash
pip install -e .
```

This installs the project with its core dependencies:
- `openai` — LLM API client
- `sounddevice` & `soundfile` — Audio processing
- `pyaudio` — Audio I/O
- `pytest` — Testing framework
- `python-dotenv` — Environment configuration

3. Set up your environment:
```bash
cp .env.example .env
# Edit .env with your API keys and configuration
```

### Running Examples

Lab notebooks use Jupyter. To run them:

```bash
jupyter notebook labs/01_hello_world/lesson1_demo.ipynb
```

Or use Python scripts directly:

```bash
python labs/01_hello_world/1_chat.py
python labs/02_standalone_agents/1_stateless_agent.py
```

### Running Tests

```bash
pytest tests/
pytest -m "not slow"  # Skip slow tests
```

## 📂 Repository Structure

```
labs/
├── 01_hello_world/          # Getting started with LLMs
├── 02_standalone_agents/    # Building agents with state
├── 03_ai-api/               # System design and integration patterns
├── 04_eval/                 # Evaluation methodologies
└── 10_lab_eval_session/     # Capstone workshop

tests/                        # Test suite
themes/                       # CSS themes for web materials

Root files:
├── AI_Design_Projects_2026.md   # Full project descriptions & rubrics
├── README.md                    # This file
├── pyproject.toml              # Project configuration
├── index.html                  # Course landing page
└── syllabus.html               # Full course syllabus
```

## 🔑 Key Concepts

### Agentic Systems
The course emphasizes building systems where AI agents:
- Make autonomous decisions and take actions
- Use external tools and APIs
- Maintain and reason about state
- Interact with humans meaningfully

### Evaluation Philosophy
Knowing whether your system works is as important as building it:
- Design alternatives (don't just try one approach)
- Honest experiments (measure what matters, admit limitations)
- Clear communication (show your work, explain trade-offs)

### Model Context Protocol (MCP)
Learn how to safely integrate tools and data sources with LLMs for building extensible, observable AI systems.

## 📖 Course Materials

- **[Syllabus](syllabus.html)** — Full course outline and grading
- **[Assessments](assessments.html)** — Grading criteria and rubrics
- **[About](about.html)** — Course philosophy and learning objectives
- **[Prompt Style Guide](prompt_style_examples.md)** — Best practices for prompt engineering

## 🛠️ Development

The course includes working code examples for:
- Chat completions and streaming LLM responses
- Voice input/output with LLMs
- Image generation and processing
- Building stateful agents with memory
- Tool use and function calling
- Long-term memory systems

See individual lab folders for complete examples and hands-on exercises.

## 📚 Further Reading

- [Lab 03: Agentic Loops & Design Patterns](labs/03_ai-api/agentic_loop.md)
- [Lab 03: Model Context Protocol Tutorial](labs/03_ai-api/mcp_tutorial.md)
- [Lab 04: Optimizing in the Dark — Evaluation Framework](labs/04_eval/optimizing-in-the-dark/)
- [Safety Guardrails for AI Systems](labs/03_ai-api/safety_guardrails.md)

## 👥 Contributing & Support

This is a University of Trento course repository. For course-related questions, contact your instructor or TA.

For issues with code examples or technical setup, open an issue in the course forum or repository.

## 📄 License

Course materials are provided for educational purposes. See individual files for specific licenses.

---

**University of Trento — 2026**

*"Ask not just whether the AI works, but how you know it works."*
