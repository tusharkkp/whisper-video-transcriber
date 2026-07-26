# Whisper Video Transcriber

A simple, user-friendly Python application that transcribes audio from video files using OpenAI's Whisper model. Select a video, and get a text transcript automatically.

## 🎯 What It Does

This tool leverages the powerful Whisper speech recognition model to automatically transcribe video files into text. It supports multiple video formats and automatically detects the language of the spoken content. The transcript is saved as a `.txt` file in the same directory as your video.

**Key Features:**
- 🎬 Supports multiple video formats (MP4, MKV, AVI, MOV, WebM)
- 🌍 Automatic language detection
- 📝 Generates clean, line-by-line transcripts
- ⚡ GPU acceleration support (optional)
- 🖱️ Simple file picker interface (no command-line arguments needed)

## 📋 Requirements

- **Python 3.8+**
- **FFmpeg** (required by Whisper to process video files)

### Python Dependencies

```
faster-whisper
```

## 🚀 Installation

### Step 1: Install FFmpeg

**macOS (using Homebrew):**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt-get install ffmpeg
```

**Windows:**
Download from [ffmpeg.org](https://ffmpeg.org/download.html) or use:
```bash
choco install ffmpeg
```

### Step 2: Clone the Repository

```bash
git clone https://github.com/tusharkkp/whisper-video-transcriber.git
cd whisper-video-transcriber
```

### Step 3: Create a Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
pip install faster-whisper
```

## 📖 Usage

Simply run the script:

```bash
python transcriber.py
```

A file picker dialog will appear. Select your video file, and the transcription will begin.

### Example Workflow

```bash
$ python transcriber.py

📂 Selected Video:
/Users/you/Videos/interview.mp4

⏳ Loading Whisper model...

🎙️ Transcribing...

🌍 Detected Language: en

✅ Done!
📝 Transcript saved to:
/Users/you/Videos/interview.txt
```

## ⚙️ Configuration

You can customize the transcriber behavior by editing `transcriber.py`:

### Model Size

Change the `MODEL_SIZE` variable (line 29):

```python
MODEL_SIZE = "base"  # Options: tiny, base, small, medium, large-v3
```

| Model | Speed | Accuracy | Memory |
|-------|-------|----------|--------|
| tiny | ⚡⚡⚡ | ⭐ | 1 GB |
| base | ⚡⚡ | ⭐⭐ | 1.4 GB |
| small | ⚡ | ⭐⭐⭐ | 2.7 GB |
| medium | 🐢 | ⭐⭐⭐⭐ | 5.1 GB |
| large-v3 | 🐢🐢 | ⭐⭐⭐⭐⭐ | 10 GB |

### GPU Acceleration

If you have an NVIDIA GPU, change line 35 from:
```python
device="cpu"
```

to:
```python
device="cuda"
```

This will significantly speed up transcription. Also update `compute_type` if desired:
```python
compute_type="float16"  # For better speed with GPU
```

### Beam Search

Adjust the `beam_size` parameter (line 46) for accuracy vs. speed trade-off:
```python
segments, info = model.transcribe(
    VIDEO_PATH,
    beam_size=5  # Higher values = more accurate but slower
)
```

## 📂 Output

- **Location:** Same directory as your input video
- **Filename:** `{original_filename}.txt`
- **Format:** Plain text, one sentence per line

Example output:
```
This is the first line of transcription.
And here is the second line.
The transcript continues line by line.
```

## 🛠️ Troubleshooting

### FFmpeg not found
**Error:** `ffmpeg not found in PATH`
**Solution:** Install FFmpeg (see Installation section) and ensure it's in your system PATH.

### Out of memory
**Error:** `CUDA out of memory` or similar memory error
**Solution:** 
- Use a smaller model size (`tiny` or `base`)
- Switch from GPU to CPU
- Reduce `beam_size` to 1

### Model download fails
**Error:** `Failed to download model`
**Solution:** 
- Check your internet connection
- Models are cached after first download in `~/.cache/huggingface/`
- Try running again after network stabilizes

### Video format not supported
**Error:** `Unsupported audio codec`
**Solution:** 
- Convert your video to MP4 format first using FFmpeg:
  ```bash
  ffmpeg -i input.mov -codec:v libx264 -codec:a aac output.mp4
  ```

## 💡 Tips & Tricks

1. **Batch Processing:** Run multiple times in sequence to transcribe multiple videos
2. **Large Files:** Consider using the `tiny` model for very large video files to save time
3. **Accuracy:** For technical content, use `small` or `medium` models
4. **Speed:** Use `tiny` or `base` with `beam_size=1` for quick previews

## 📊 Performance

Approximate transcription times on different hardware:

| Model | CPU (M1 Mac) | GPU (RTX 3080) |
|-------|---|---|
| tiny | 30s for 10 min video | 5s |
| base | 1-2 min for 10 min video | 10s |
| small | 3-5 min for 10 min video | 20s |

## 🔧 Technical Stack

- **[faster-whisper](https://github.com/SYSTRAN/faster-whisper)** - Optimized Whisper implementation
- **[tkinter](https://docs.python.org/3/library/tkinter.html)** - GUI file picker
- **[pathlib](https://docs.python.org/3/library/pathlib.html)** - File path handling

## 📝 License

This project is open source. Feel free to use, modify, and distribute as needed.

## 🤝 Contributing

Found a bug or have a feature suggestion? Feel free to open an issue or submit a pull request!

## 🙏 Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper) - The underlying speech recognition model
- [faster-whisper](https://github.com/SYSTRAN/faster-whisper) - Optimized implementation

## ❓ FAQ

**Q: Can it handle videos with multiple languages?**
A: Yes, Whisper will transcribe in the detected language. For mixed-language content, transcription may switch between languages.

**Q: What's the maximum video length?**
A: There's no hard limit, but longer videos require more processing time. Very long videos (2+ hours) may need optimizations.

**Q: Can I use this offline?**
A: After downloading the model on your first run, the tool works completely offline.

**Q: Does it preserve timestamps?**
A: The current version outputs plain text. For timestamped output, you can modify the script to save segment timestamps.

---

**Happy transcribing! 🎉**
