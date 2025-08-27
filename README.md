# MindScrole V1.1 - Instagram Reel Transcript MVP

MindScrole is an AI-powered tool designed to extract and display transcripts from Instagram Reels.  
This MVP allows users to submit a Reel URL and receive a **full transcript** of the video directly on a web dashboard built with **Streamlit**.

---

## 🚀 Features (V1.1)
- Accept Instagram Reel URLs as input
- Download the reel video
- Extract audio from the video
- Generate a **text transcript** using **OpenAI Whisper**
- Display transcript on a **Streamlit dashboard**
- Clean up video/audio files after processing

> ⚡ Note: This is a **manual MVP** intended for 3–5 users. Summarization and advanced organization will come in future versions.

---

## 🛠 Tech Stack
- **Frontend & Hosting:** Streamlit Cloud  
- **Video Download:** `yt-dlp`  
- **Audio Extraction:** `moviepy` / `ffmpeg`  
- **Transcription:** OpenAI Whisper (Python library)  
- **Version Control & Deployment:** GitHub / Gitrope + Streamlit Cloud

---

## 📦 Installation (Local)
1. Clone the repository:
```bash
git clone <https://github.com/manthank17-learn/mindscrole.git>
cd mindscroll
```

## Install Dependencies 
```bash
pip install -r requirements.txt
```

## Run the Streamlit app locally:
```bash
streamlit run app.py
```
---

## 💻 Usage
1.Open the app in Streamlit (local or deployed link)

2.paste an Instagram Reel URL into the input box

3.Click "Get Transcript"

4.Wait a few seconds for processing

5.Transcript will appear on the dashboard

Optional: copy or download the transcript

---

## ⚙️ Workflow (V1.1)

1.User submits Instagram Reel link

2.Python backend downloads the video using yt-dlp

3.Extracts audio using moviepy

4.Transcribes audio using OpenAI Whisper

5.Displays transcript in Streamlit UI

6.Video/audio files are deleted to save space

---


##⚙️ Workflow (V1.1)

User submits Instagram Reel link

Python backend downloads the video using yt-dlp

Extracts audio using moviepy

Transcribes audio using OpenAI Whisper

Displays transcript in Streamlit UI

Video/audio files are deleted to save space

---

 ## 🔜 Roadmap / Future Enhancements

1.Automatic summarization of transcript

2.Topic categorization / tagging

3.Calendar integration for review

4.GitHub repo as a versioned knowledge vault

5.Multi-user support with authentication

6.Browser extension / mobile app integration

---

 ## ⚠️ Limitations (V1.1)

1.Only supports manual submission of links

2.Not optimized for large-scale automation

3.Reel download may fail if Instagram link is private or blocked

4.Whisper transcription accuracy may vary for background noise or accents

---

## 📧 Contact

For questions or collaboration, reach out at: mindscrole@gmail.com
