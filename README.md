# Hugging Face Agents - VS Code Integration Guide

> **Hugging Face Agent Course - Unit 4 Assignment**

This repository contains a comprehensive guide for integrating Hugging Face agents with Visual Studio Code, completed as part of Unit 4 of the Hugging Face Agent Course.

## 📋 Overview

This project demonstrates how to set up, configure, and use Hugging Face agents within VS Code, providing a practical workflow for developing AI-powered applications with agent capabilities.

## 🎯 Learning Objectives

- Understand Hugging Face agent architecture
- Configure VS Code for agent development
- Implement practical agent workflows
- Debug and test agents effectively
- Deploy agents in production environments

## 🚀 Prerequisites

Before getting started, ensure you have:

- **Python 3.8+** installed
- **Visual Studio Code** (latest version recommended)
- **Hugging Face account** (for API access)
- Basic understanding of:
  - Python programming
  - AI/ML concepts
  - Command-line operations

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/hf-agents-vscode-guide.git
cd hf-agents-vscode-guide
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set your token as an environment variable:

```bash
export HUGGINGFACE_TOKEN="your_token_here"
```

## 🛠️ VS Code Setup

### Required Extensions

Install these VS Code extensions for optimal development:

- **Python** (Microsoft)
- **Pylance** (Microsoft)
- **Jupyter** (Microsoft)
- **GitLens** (optional, for version control)

### Recommended Settings

Add to your `settings.json`:

```json
{
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.formatting.provider": "black",
  "editor.formatOnSave": true
}
```

## 💡 Usage

### Basic Agent Example

```python
from transformers import HfAgent

# Initialize the agent
agent = HfAgent("https://api-inference.huggingface.co/models/bigcode/starcoder")

# Run a task
agent.run("Generate a python function to calculate fibonacci numbers")
```

### Running the Guide

1. Open the HTML guide in your browser:
   ```bash
   open hf_agents_vscode_guide.html
   ```

2. Follow the step-by-step instructions
3. Execute code examples in VS Code
4. Experiment with different agent configurations

## 📚 Project Structure

```
hf-agents-vscode-guide/
├── README.md
├── hf_agents_vscode_guide.html    # Main guide
├── requirements.txt                # Python dependencies
├── examples/                       # Code examples
│   ├── basic_agent.py
│   ├── custom_tools.py
│   └── advanced_workflows.py
├── notebooks/                      # Jupyter notebooks
│   └── agent_exploration.ipynb
└── assets/                         # Images and resources
    └── screenshots/
```

## 🔧 Features

- ✅ Complete setup instructions for VS Code
- ✅ Practical code examples
- ✅ Integration with Hugging Face Inference API
- ✅ Custom tool development
- ✅ Debugging techniques
- ✅ Best practices and optimization tips

## 🎓 Assignment Completion

This project fulfills the Unit 4 requirements by:

1. **Setting up a development environment** for Hugging Face agents
2. **Implementing agent workflows** in VS Code
3. **Creating practical examples** of agent usage
4. **Documenting the process** in an accessible format
5. **Demonstrating understanding** of agent architecture

## 🐛 Troubleshooting

### Common Issues

**Problem**: Import errors with transformers
```bash
pip install --upgrade transformers
```

**Problem**: API rate limiting
- Use your Hugging Face token
- Consider using a local model
- Implement retry logic with exponential backoff

**Problem**: VS Code Python interpreter not found
- Open Command Palette (Ctrl+Shift+P)
- Search "Python: Select Interpreter"
- Choose your virtual environment

## 📖 Resources

- [Hugging Face Agent Documentation](https://huggingface.co/docs/transformers/transformers_agents)
- [Hugging Face Agent Course](https://huggingface.co/learn/agents-course)
- [Transformers Library](https://github.com/huggingface/transformers)
- [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)

**Course**: Hugging Face Agent Course  
**Unit**: 4 - Agent Development with VS Code  
**Status**: ✅ Completed  
**Date**: April 2026
