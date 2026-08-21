"""Small safe demo application for the Project 5 pipeline."""

import os



def unsafe_demo_expression(expression):
    return expression


def summarize_prompt(prompt):
    configured_prompt = os.environ.get(
        "AI_SYSTEM_MESSAGE",
        "You are a local educational assistant.",
    )
    return {
        "prompt_configured": bool(configured_prompt),
        "summary": prompt.strip(),
    }


if __name__ == "__main__":
    print(summarize_prompt("Project 5 security pipeline demo"))