from faster_whisper import WhisperModel
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from pathlib import Path
import sys

# -----------------------------
# Select Video File
# -----------------------------
Tk().withdraw()

VIDEO_PATH = askopenfilename(
    title="Select a Video",
    filetypes=[
        ("Video Files", "*.mp4 *.mkv *.avi *.mov *.webm"),
        ("All Files", "*.*")
    ]
)

if not VIDEO_PATH:
    print("❌ No video selected.")
    sys.exit()

print(f"\n📂 Selected Video:\n{VIDEO_PATH}")

# -----------------------------
# Load Whisper Model
# -----------------------------
MODEL_SIZE = "base"  # tiny, base, small, medium, large-v3

print("\n⏳ Loading Whisper model...")

model = WhisperModel(
    MODEL_SIZE,
    device="cpu",          # Change to "cuda" if you have an NVIDIA GPU
    compute_type="int8"
)

# -----------------------------
# Transcribe
# -----------------------------
print("🎙️ Transcribing...\n")

segments, info = model.transcribe(
    VIDEO_PATH,
    beam_size=5
)

print(f"🌍 Detected Language: {info.language}")

# -----------------------------
# Save Transcript
# -----------------------------
output_file = Path(VIDEO_PATH).with_suffix(".txt")

with open(output_file, "w", encoding="utf-8") as f:
    for segment in segments:
        f.write(segment.text.strip() + "\n")

print("\n✅ Done!")
print(f"📝 Transcript saved to:\n{output_file}")