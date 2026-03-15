from pathlib import Path

from src.video_utils import ensure_file_exists, run_command


def stitch_videos(
    first_video_path: str,
    second_video_path: str,
    output_video_path: str
) -> str:
    
    ensure_file_exists(first_video_path)
    ensure_file_exists(second_video_path)


    output_path = Path(output_video_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)


    concat_file = output_path.parent / "concat_list.txt"
    

    concat_file.write_text(
        f"file '{Path(first_video_path).resolve().as_posix()}'\n"
        f"file '{Path(second_video_path).resolve().as_posix()}'\n",
        encoding="utf-8"
    )



    command = [
        "ffmpeg",
        "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", str(concat_file),
        "-c:v", "libx264",
        "-c:a", "aac",
        output_video_path
    ]

    run_command(command)



    if concat_file.exists():
        concat_file.unlink()


    return str(output_path)
