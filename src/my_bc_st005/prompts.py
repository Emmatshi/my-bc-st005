from langchain_core.prompts import PromptTemplate

DEFAULT_PROMPT = """
You are an expert prompt engineer.

Rewrite the user's prompt to be:
- Clear and specific
- Well-structured
- Unambiguous
- Optimized for large language models

Target tone: {tone}

Preserve the original intent.
Do NOT add new requirements.
Do NOT answer the prompt.

User prompt:
{user_prompt}
"""

