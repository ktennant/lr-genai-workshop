import vertexai
from vertexai.generative_models import GenerativeModel, Part
import vertexai.generative_models as generative_models


def generate():
    vertexai.init(project="global-sre-dev", location="us-central1")
    model = GenerativeModel("gemini-1.0-pro-001")
    responses = model.generate_content(
        """You are a comedian who isn\'t very funny because you always try to explain the punchline of a joke.  Make sure to explain why the joke was funny in case the user did not understand.

Tell me a joke.""",
        generation_config={"max_output_tokens": 2048, "temperature": 0.1, "top_p": 1},
        safety_settings={
            generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        },
        stream=True,
    )

    for response in responses:
        print(response.text, end="")


generate()
