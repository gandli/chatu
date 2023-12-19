import os
import g4f
from rich.console import Console
from rich.markdown import Markdown

def get_response(message, model="gpt-3.5-turbo"):
    yield from g4f.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": message}],
        stream=True,
    )

if __name__ == "__main__":
    console = Console()
    message = r"""
    """
    answer = ""
    for result in get_response(message, "gpt-4"):
        os.system("clear")
        answer += result
        md = Markdown(answer)
        console.print(md, no_wrap=False)