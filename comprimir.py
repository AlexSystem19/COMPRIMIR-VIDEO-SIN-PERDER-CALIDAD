import subprocess
import os
from pathlib import Path

videos = [
    r"D:\TU_CARPETA\video1.mkv",
    r"D:\TU_CARPETA\video2.mkv",
]

for video in videos:
    input_file = Path(video)
    output = str(input_file.parent / f"{input_file.stem}_compressed.mp4")
    size_in = os.path.getsize(video) / (1024 ** 3)
    print(f"\n▶ Procesando: {input_file.name}  ({size_in:.2f} GB)")

    cmd = [
        "ffmpeg", "-y", "-i", video,
        "-vcodec", "libx265", "-crf", "32",
        "-preset", "medium",
        "-vf", "scale='min(1920,iw)':-2",
        "-r", "24",
        "-acodec", "aac", "-b:a", "96k", "-ac", "1",
        "-tag:v", "hvc1",
        output
    ]

    subprocess.run(cmd)
    size_out = os.path.getsize(output) / (1024 ** 3)
    print(f"✅ Listo: {size_out:.2f} GB → {output}")

print("\n🎯 Ambos videos procesados.")