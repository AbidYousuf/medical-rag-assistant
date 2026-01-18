# # llm/ollama_client.py
# import subprocess

# class OllamaClient:
#     """
#     Client to interact with Ollama via CLI.
#     """

#     def __init__(self, model_name: str = "gemma3:4b"):
#         self.model_name = model_name

#     def generate(self, prompt: str) -> str:
#         result = subprocess.run(
#             ["ollama", "run", self.model_name],
#             input=prompt,
#             text=True,
#             capture_output=True
#         )
#         return result.stdout.strip()
# llm/ollama_client.py
import subprocess

class OllamaClient:
    def __init__(self, model_name: str = "gemma3:4b"):
        self.model_name = model_name

    def generate(self, prompt: str) -> str:
        result = subprocess.run(
            ["ollama", "run", self.model_name],
            input=prompt.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return result.stdout.decode("utf-8", errors="ignore").strip()
