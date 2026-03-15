from pathlib import Path
import shutil
import os
from dotenv import load_dotenv
import fal_client
import requests



from src.video_utils import ensure_file_exists

load_dotenv()

def mock_generation_ending(
        source_video_path: str,
        output_video_path: str

) -> str:
    
    ensure_file_exists(source_video_path)
    output_path = Path(output_video_path)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_video_path, output_path)

    return str(output_path)


def generate_ending_with_fal(
    image_path: str,
    prompt: str,
    output_video_path: str
) -> str:
    ensure_file_exists(image_path)

    fal_key = os.getenv("FAL_KEY")
    if not fal_key:
        raise RuntimeError("FAL_KEY is missing , add it into you .env file.")
    output_path = Path(output_video_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    os.environ["FAL_KEY"] = fal_key


    image_url = fal_client.upload_file(image_path)




    result = fal_client.subscribe(
        "fal-ai/wan/v2.2-5b/image-to-video",
        arguments={
            "image_url": image_url,
            "prompt": prompt,
            "resolution": "580p",
            "num_frames": 41,
            "frames_per_second": 16,
            "aspect_ratio": "auto"
        }
    )


    video_url = result["video"]["url"]
    response = requests.get(video_url, timeout=120)
    response.raise_for_status()



    with open(output_path, "wb") as f:
        f.write(response.content)

    return str(output_path)