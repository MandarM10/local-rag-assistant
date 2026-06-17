from dotenv import load_dotenv
from local_llm import AiModel

load_dotenv()

print("Loading model...")

model = AiModel()

print("Model loaded!")

model.ask_a_question("What is Big Data?")