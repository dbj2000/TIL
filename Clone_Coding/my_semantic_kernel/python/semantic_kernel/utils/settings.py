from typing import Optional, Tuple

def openai_settings_from_dot_env() -> Tuple[str, Optional[str]]:
    """
    Reads the OpenAI API key and organization ID from the .env file.

    Returns:
        Tuple[str, str]: The OpenAI API key, the OpenAI organization ID
    """

    api_key, org_id = None, None
    with open("/Users/jin/git/TIL/Clone_Coding/my_semantic_kernel/python/.env", "r") as f:
        lines = f.readlines()

        for line in lines:
            if line.startswith("OPENAI_API_KEY"):
                parts = line.split("=")[1:]
                api_key = "=".join(parts).strip().strip('"')
                continue

            if line.startswith("OPENAI_ORG_ID"):
                parts = line.split("=")[1:]
                org_id = "=".join(parts).strip().strip('"')
                continue

    assert api_key is not None, "OpenAI API key not found in .env file"

    return api_key, org_id