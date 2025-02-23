# hf_smolagents

# hf_smolagents

## Overview
`hf_smolagents` is a collection of highly specialized Python tools designed to automate various tasks efficiently using AI-driven agents. The agents can perform complex problem-solving, such as retrieving information from the web, interacting with APIs, performing data manipulations, and generating results from complex tools, with an emphasis on usability and streamlined integration.

The repository provides an extensible framework for incorporating AI capabilities into various workflows, and it is built with the flexibility to add new tools and models as needed.

## Key Features
- **Modular Tools**: The project includes several tools, such as `DuckDuckGoSearchTool`, `HfApiModel`, and custom tools for time conversion (`get_current_time_in_timezone`) and space exploration countdowns (`get_launch_time`).
- **AI-driven Task Automation**: Using a structured `Thought:`, `Code:`, and `Observation:` framework, the agents tackle tasks step-by-step.
- **Integration with Gradio**: User-friendly interfaces for interaction with AI agents through Gradio.
- **Extensible Agent Framework**: The architecture allows for seamless extension with new tools and models to solve unique tasks.

## Setup
To get started with `hf_smolagents`, clone this repository and install the necessary dependencies:

```bash
git clone https://github.com/yourusername/hf_smolagents.git
cd hf_smolagents
pip install -r requirements.txt
