from my_bc_st005.llm import get_llm
from my_bc_st005.prompts import DEFAULT_PROMPT


def refine_prompt(user_prompt: str, tone: str) -> str:
    llm = get_llm()

    formatted_prompt = DEFAULT_PROMPT.format(
        user_prompt=user_prompt.strip(),
        tone=tone
    )

    try:
        response = llm.invoke(formatted_prompt)
        return response.content.strip()

    except Exception as exc:
        return(
            "⚠️ Unable to refine the prompt at this time.\n\n"
            f"Details: {exc}"
            )
        

        



