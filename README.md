# OpenAssistant Demo

This is just a demo on using OpenAssistant with langchain on huggingface 

# Setup

### 1. Install Dependencies

```bash
pip install -U pdm
pdm sync
```
### 2. filling in hugging face api key

```bash
cp .env.dist .env
vim .env
```
### 3. Ask a question

```bash
pdm run main.py "Hi, Ask me a question instead"
```
