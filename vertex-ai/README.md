# Vertex AI and Gemini

## Prompting in the GCP Console

- Navigate to [Vertext AI Studio](https://console.cloud.google.com/vertex-ai/generative?project=global-sre-dev) in `global-sre-dev`
- Select "Language"
- Select "Create a new text prompt"
- Use the following prompt

```text
You are a comedian who isn't very funny because you always try to explain the punchline of a joke.  Make sure to explain why the joke was funny in case the user did not understand.

Tell me a joke.
```

## Moving from Console to App

- Select "Get Code" and copy the output to your clipboard

### Create a Python Env

Note: You may need to run `deactivate` if the previous virtual environment is still active.

```shell
mkdir workshop2 && cd workshop2
virtualenv .venv
source .venv/bin/activate
```

### Create the App

```shell
echo "google-cloud-aiplatform" > requirements.txt
pip install -r requirements.txt
touch jokes.py
```

Copy the contents of clipboard into `jokes.py` then run:

```
python jokes.py
```

### Convert to LangChain

- Add `langchain_core` and `langchain-google-vertexai` to `requirements.txt`
- Install packages using `pip install -r requirements.txt`
- Add the following imports:

```python
from langchain_core.prompts import PromptTemplate
from langchain_google_vertexai import VertexAI
```

- Modify code using at a minimum:

```python
prompt = PromptTemplate.from_template(
    """
    You are a comedian who is not very funny because you always try to explain the punchline of a joke.  Make sure to explain why the joke was funny in case the user did not understand.
    Tell me a joke about {subject}.
    """)
llm = VertexAI(model_name="gemini-pro")

# LangChain Expression Language (LCEL)
chain = prompt | llm

subject = input("What do you want to hear a joke about?: ")
print(chain.invoke({'subject': subject}))
```

- Templatetize the Promp
