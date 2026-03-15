def build_video_prompt(user_prompt: str) -> str:
    cleaned_prompt = user_prompt.strip()


    if not cleaned_prompt:
        raise ValueError("User prompt cannot be empty")
    

    base_prompt = (
        "cinematic continuation of the final scene, "
        "same environment, consistent lighting, "
        "smooth transition from the original video, "
        "realistic motion, detailed visual storytelling, "
    )


    final_prompt = base_prompt + cleaned_prompt

    return final_prompt