from src.prompt_builder import build_video_prompt

user_prompt = "make the ending happy with a reunion"

final_prompt = build_video_prompt(user_prompt)

print("User prompt:")
print(user_prompt)
print()
print("Final prompt:")
print(final_prompt)