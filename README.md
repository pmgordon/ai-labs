# Langgraph Labs

This repo has various bite sized tests that can help one build up knowledge of langraph, langchain and function calling. It runs completly locally using the `llama3.2:3b-instruct-fp16` Library

## Topics

* Vector Database with OpenSearch
* Tools
* Nodes
* Document Retrievers
* Function calling
* Graphs

## Running Locally

### Run Ollama

Install ollama
```
brew install ollama
```

Run `llama3.2:3b-instruct-fp16`
```
ollama start
ollama run llama3.2:3b-instruct-fp16
```


## Run Docker
Start OpenSearch Docker

```
docker compose up
```


## Function calling

* Make a python virtual environment at .pyenv -> `make init`
* Source the python virtual environment `source .pyenv/bin/activate`
* Install requirements `make pipreq` 

## Test
### Run All Tests
To run all tests execute `make test`

### Coverage Report
To run all tests execute `make coverage`