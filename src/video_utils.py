from pathlib import Path
import subprocess




def ensure_file_exists(video_path: str) -> Path:
    path = Path(video_path)
    if not path.exists():
        raise FileNotFoundError(f"Video file not found: {video_path}")
    if not path.is_file():
        raise ValueError(f"Path is not a file: {video_path}")
    return Path

def run_command(command: list[str]) -> None:
    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    if result.returncode !=0:
        raise RuntimeError(

            f"command failed.  \nSTDOUT: \n{result.stdout} \nSTDERR: \n{result.stderr}"

        )
    


def get_video_duration(video_path: str) -> float:
    ensure_file_exists(video_path)

    command = [
        "ffprobe", "-v","error","-show_entries", "format=duration","-of","default= noprint_wrappers=1:nokey=1", video_path
    ]

    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"could not get video duration.\nSTDERR:\n{result.stderr}"
        )
    try:
        return float(result.stdout.strip())
    except ValueError as exc:
        raise RuntimeError("Failed to prase video duration.") from exc




def extract_last_n_seconds(
    input_video_path: str,
    output_video_path: str,
    seconds_to_extract: int = 5
) -> str:
        duration = get_video_duration(input_video_path)
        if seconds_to_extract <= 0:
            raise ValueError("seconds_to_extract must be greater than 0")
        if duration <= seconds_to_extract:
            raise ValueError(f"Video is too short . Duration is{duration:.2f}s, cannot extract last{seconds_to_extract}s.")
        
        start_time = duration - seconds_to_extract

        output_path = Path(output_video_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        command = [
            "ffmpeg","-y","-ss", str(start_time), "-i", input_video_path,
            "-t", str(seconds_to_extract),"-c:v","libx264","-c:a","aac",
            output_video_path
        ]


        run_command(command)
        return str(output_path)



def remove_last_n_seconds(
        input_video_path: str,
        output_video_path: str,
        seconds_to_remove: int =5
) -> str:
    

    duration = get_video_duration(input_video_path)
    if seconds_to_remove <= 0:
        raise ValueError("seconds_to_remove must be greater than 0")
    
    if duration <= seconds_to_remove:
        raise ValueError(f"Video is too short. Duration is {duration:.2f}s, cannot remove last {seconds_to_remove}s."
        )
    
    keep_duration = duration - seconds_to_remove

    output_path = Path(output_video_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)


    command = [
        "ffmpeg", "-y", "-i", input_video_path,
        "-t", str(keep_duration), "-c:v", "libx264",
        "-c:a", "aac",
        output_video_path
    ]


    run_command(command)

    return str(output_path)