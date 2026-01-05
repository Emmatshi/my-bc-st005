from my_bc_st005.llm import get_llm
from my_bc_st005.prompts import DEFAULT_PROMPT


def refine_prompt(user_prompt: str) -> str:
    llm = get_llm()

    formatted_prompt = DEFAULT_PROMPT.format(
        user_prompt=user_prompt.strip()
    )

    response = llm.invoke(formatted_prompt)

    return response.content.strip()



