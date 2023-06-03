# OpenAssistant Demo

This is just a demo on using OpenAssistant with langchain on huggingface 

# install dependencies
```bash
pip install -U pdm
pdm sync
```

fill in the env var after copying the .env file
```bash
cp .env.dist .env
```
get your huggingface api key and write it in the .env file
```bash
pdm run main.py "Hi, Ask me a question instead"
```