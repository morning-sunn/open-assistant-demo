import typer
from decouple import config
from langchain import PromptTemplate, HuggingFaceHub, LLMChain


def make_oa_chain():
    template = """<|prompter|>{question}<|endoftext|>
        <|assistant|>"""

    prompt_template = PromptTemplate(template=template, input_variables=["question"])

    open_assistant = HuggingFaceHub(
        repo_id="OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5",
        huggingfacehub_api_token=config('hf_api_key'),
        model_kwargs={
            'max_new_tokens': 800
        }
    )

    oa_chain = LLMChain(
        llm=open_assistant,
        prompt=prompt_template
    )
    return oa_chain


def main(question: str = typer.Argument(..., help="The question to ask the language model.")):
    oa_chain = make_oa_chain()
    response = oa_chain.run(question)
    print(response)


if __name__ == '__main__':
    typer.run(main)
