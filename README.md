# OpenAssistant Demo

This is just a demo on using OpenAssistant with langchain on huggingface 

# Setup

### 1. Install Dependencies

```bash
pip install -U pdm
pdm sync
```
### 2. Fill in HuggingFace inference api key
obtaining an Inference API key: https://huggingface.co/docs/api-inference/quicktour#get-your-api-token

```bash
cp .env.dist .env
vim .env
```
### 3. Ask a question

```bash
pdm run main.py "Hi, Ask me a question instead"
```
