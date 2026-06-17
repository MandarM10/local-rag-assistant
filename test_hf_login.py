# test_hf_login.py

from dotenv import load_dotenv
import os
from huggingface_hub import login

load_dotenv()

token = os.getenv("HF_TOKEN")

print("Token found:", bool(token))

login(token=token)

print("Login successful!")