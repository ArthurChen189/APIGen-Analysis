# APIGen Analysis

A comprehensive post-mortem analysis toolkit for the APIGen pipeline, focusing on evaluating and understanding API generation patterns and performance metrics.

## Overview

This repository contains tools and notebooks for analyzing the APIGen pipeline, which is designed to generate API calls from natural language descriptions. Our analysis provides insights into the model's performance, behavior patterns, and potential areas for improvement. It also mainly focusing on answering the following questions:
- What is the distribution of questions, backlog tools, and answers of naturally existing data vs. synthesized data?
- How to define the complexity of APIs?
- How to move beyond queries LLM can generate?

## Prerequisites

- Python 3.11 or higher

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ArthurChen189/APIGen-Analysis.git
cd APIGen-Analysis
```

2. Initialize and update submodules:
```bash
git submodule update --init --recursive
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

The main analysis can be found in our Jupyter notebook:
- [analysis.ipynb](analysis.ipynb) - Contains detailed analysis, visualizations, and findings

To run the analysis:
1. Launch Jupyter Notebook or Jupyter Lab
2. Open `analysis.ipynb`
3. Follow the step-by-step instructions in the notebook

## Project Structure

```
APIGen-Analysis/
├── analysis.ipynb     # Main analysis notebook
├── requirements.txt   # Python dependencies
├── smt_generator.py   # Script for generating API calls via SMT solver
├── gorilla/          # Gorilla codebase for API generation and evaluation
├── Salesforce_xLAM-7B-fc-r/ # Salesforce xLAM-7B-fc-r API generation results in JSON format
└── ...
```

## References

- [APIGen: Automated Pipeline for Generating Verifiable and Diverse Function-Calling Datasets](https://arxiv.org/abs/2406.18518)
- [Gorilla: Large Language Model Connected with Massive APIs](https://github.com/ShishirPatil/gorilla/tree/main)
