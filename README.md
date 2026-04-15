# Python + ffmpeg — Comprime video sin pagar nada

> 7 GB → 170 MB. Resultado real. Probado en grabaciones de sala con Excel en pantalla.

---

## El problema

Gemini tiene un límite de **2 GB** por archivo.  
Las grabaciones de reuniones o presentaciones fácilmente superan los 6–7 GB.  
La mayoría de soluciones que encuentras online son de pago, lentas, o suben tu video a un servidor de alguien más.

Esta no.

---

## Lo que necesitas

- Python instalado
- ffmpeg instalado

```bash
# Windows
winget install ffmpeg

# Verificar
ffmpeg -version
```

---

## El script

Guarda esto como `comprimir.py` en la misma carpeta que tus videos:

```python
import subprocess
import os
from pathlib import Path

videos = [
    r"D:\TU_CARPETA\video1.mkv",
    r"D:\TU_CARPETA\video2.mkv",
]

for video in videos:
    f = Path(video)
    out = str(f.parent / f"{f.stem}_compressed.mp4")
    size_in = os.path.getsize(video) / (1024 ** 3)
    print(f"\n▶ {f.name}  ({size_in:.2f} GB)")

    subprocess.run([
        "ffmpeg", "-y", "-i", video,
        "-vcodec", "libx265",
        "-crf", "32",
        "-preset", "medium",
        "-r", "24",
        "-acodec", "aac",
        "-b:a", "96k",
        "-ac", "1",
        "-tag:v", "hvc1",
        out
    ])

    size_out = os.path.getsize(out) / (1024 ** 3)
    print(f"✅ {size_out:.2f} GB → {out}")
```

Cambia las rutas. Corre:

```bash
python comprimir.py
```

---

## Por qué funciona

H.265 (HEVC) es mucho más eficiente que H.264, el codec que usan la mayoría de grabaciones por defecto.  
Cuando el video tiene poco movimiento — personas sentadas, pantallas con Excel, presentaciones — el codec colapsa los frames repetidos casi sin pérdida visible.

El codec no trabaja más de lo necesario.

---

## Parámetro CRF — ajusta según tu caso

| CRF | Cuándo usarlo |
|-----|---------------|
| `26` | Texto en pantalla que debe verse nítido |
| `32` | Punto dulce para reuniones y presentaciones ← recomendado |
| `36` | Solo importa el tamaño, calidad secundaria |

---

## Resultado real

| Archivo | Original | Comprimido | Reducción |
|---------|----------|------------|-----------|
| Grabación sala + Excel (1h 40min) | 7.1 GB | 0.17 GB | 97% |

---

## Notas

- Los archivos comprimidos se guardan en la misma carpeta con el sufijo `_compressed.mp4`
- Compatible con MKV, MP4, AVI y la mayoría de formatos de entrada
- Tiempo estimado: 15–30 minutos por video según CPU
- Sin subir nada a ningún servidor. Todo local.

---

*by [UXDEVOPS](https://uxdevops.com)*
