# Up and Running with LLMs

## Basic Concepts

### AI, Generative AI, AGI, oh my

Let's go ask an AI!

> AI (Artificial Intelligence): This is a broad term that encompasses any computer system or machine with the ability to perform tasks that typically require human intelligence. This includes problem-solving, recognizing speech, translating languages, and more.
>
> Generative AI: This is a subset of AI focused on creating new content, whether that be text, images, music, or other forms of media. It uses machine learning to generate outputs that are novel and often indistinguishable from those created by humans.
>
> LLMs (Large Language Models): These are a type of generative AI that specifically deal with understanding and generating human language. They are trained on vast amounts of text data and can perform tasks like translation, summarization, question-answering, and content creation.
>
> AGI (Artificial General Intelligence): This is the concept of a machine with the ability to understand, learn, and apply knowledge in a way that is indistinguishable from a human across any field of intellectual endeavor. Unlike the other terms, AGI is still theoretical and represents a future state where AI can perform any intellectual task that a human can.

### Models

For context, this workshop is only going to be discussing LLMs. However, it's worth pointing out that in the AI space, there are a variety of othery types of models such as:

- Machine Learning (ML) Models
- Deep Learning Models
- Probabilistic Models
- Graphical Models (not pictures, graphs of data)
- and more!

### Prompting

#### Prompts

Prompts are the instructions we send to an LLM to get a response back.

#### Prompt Templates

A prompt template is a pre-designed set of instructions that contains tokens as placeholders that will be replaced by user input.

#### Prompt Engineering

Prompt engineering is the practice of crafting prompts to effectively communicate with and elicit desired responses from an LLM. It is an iterative process of experimenting with and refining the prompt based on the model's output. Often includes the use of prompt templates.

### Retrieval Augmented Generation (RAG)

The only input to an LLM is a prompt. If you want an LLM to review certain context (such as a document) and provide output based on that context it's often times too large to send the entire text in a prompt. Retrieval Augmented Generation solves this by using semantic searching over a dataset and only providing a small portion of the entire dataset to the LLM based on the search result.

### Hugging Face

[Hugging Face](https://huggingface.co/models). is the Docker Hub of LLMs. All models on Hugging Face are open sourced and publicly available. It also contains community supported large datasets that can be used for fine-tuning.

### Foundational Models and Fine Tuning

LLMs that we'll talk about and use in this workshop are "Foundational Models" which are usually produced by larger organizations that have the compute to create these types of models trained on large datasets. Examples of foundational models include Llama2, Mistral, Open Sora, Gemma, etc. Fine tuned models are foundational models that have had additional training by specific datasets.

### Frameworks

- [LangChain](https://python.langchain.com/docs/get_started/introduction)
  - broad in scope, a very mature framework with a large community
  - Can use [LangChain Expression Language](https://python.langchain.com/docs/expression_language/why)
- [Llama Index](https://docs.llamaindex.ai/en/stable/)
  - narrow focused; opinionated framework with reasonable defaults make it very easy to use
  - less easy when you want to go out the box
  - can be used to compliment LangChain (they are not exclusive)
  - [Llama Hub](https://llamahub.ai/) is awesome for setting up just about any kind of RAG pipeline you can dream

## Workshop Projects

- [Running LLM Locally](./local-llm/README.md)
- [RAG pipeline with Ollama and Llama Index](./local-rag/README.md)
- [Vertex AI with Gemini](./vertex-ai/README.md)
