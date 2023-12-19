import re
import g4f
import config

def get_response(message, **kwargs):
    yield from g4f.ChatCompletion.create(
        model=config.GPT_ENGINE,
        messages=[{"role": "user", "content": message}],
        stream=True,
    )

def bing(response):
    response = re.sub(r"\[\^\d+\^\]", "", response)
    if len(response.split("\n\n")) >= 2:
        return "\n\n".join(response.split("\n\n")[1:])
    else:
        return response

if __name__ == "__main__":

    message = """

    """
    answer = ""
    for result in get_response(message, "gpt-4"):
        print(result, end="")