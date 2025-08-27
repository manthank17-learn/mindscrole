import os
import streamlit as st
from yt_dlp import YoutubeDL
from moviepy.audio.io.AudioFileClip import AudioFileClip
import whisper
import tempfile
import shutil

# Page configuration
st.set_page_config(
    page_title="MindScrole - Instagram Reel Transcriber",
    page_icon="🎬",
    layout="wide"
)

# Title and description
st.title("🎬 MindScrole V1.1")
st.markdown("**AI-powered Instagram Reel Transcript Generator**")
st.markdown("---")

# Sidebar with info
with st.sidebar:
    st.header("ℹ️ How it works")
    st.markdown("""
    1. Paste Instagram Reel URL
    2. Click 'Get Transcript'
    3. Wait for processing
    4. View your transcript!
    """)
    st.markdown("---")
    st.markdown("**Tech Stack:**")
    st.markdown("- OpenAI Whisper")
    st.markdown("- yt-dlp")
    st.markdown("- MoviePy")
    st.markdown("- Streamlit")

# Main interface
st.header("📝 Generate Transcript")

# URL input
reel_url = st.text_input(
    "Video URL:",
    placeholder="https://www.instagram.com/reel/... or YouTube/TikTok URL",
    help="Paste Instagram Reel, YouTube, or TikTok URL here"
)

st.info("💡 **Tip:** If Instagram fails due to rate limits, try YouTube Shorts or TikTok URLs!")

# Process button
if st.button("🚀 Get Transcript", type="primary"):
    if not reel_url:
        st.error("❌ Please enter a valid Instagram Reel URL")
    else:
        # Create progress bar
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        try:
            # Create temporary directory for processing
            with tempfile.TemporaryDirectory() as temp_dir:
                
                # Step 1: Download video
                status_text.text("📥 Downloading video...")
                progress_bar.progress(20)
                
                video_path = os.path.join(temp_dir, "reel_video.%(ext)s")
                ydl_opts = {
                    "outtmpl": video_path,
                    "quiet": True,  # Suppress yt-dlp output
                    "extractor_args": {
                        "instagram": {
                            "api_version": "v1"
                        }
                    },
                    "http_headers": {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                    }
                }
                
                with YoutubeDL(ydl_opts) as ydl:
                    ydl.download([reel_url])
                
                # Find the downloaded video file
                video_file = None
                for file in os.listdir(temp_dir):
                    if file.startswith("reel_video"):
                        video_file = os.path.join(temp_dir, file)
                        break
                
                if not video_file:
                    st.error("❌ Failed to download video. Please check the URL.")
                    st.stop()
                
                # Step 2: Extract audio
                status_text.text("🎵 Extracting audio...")
                progress_bar.progress(40)
                
                audio_file = os.path.join(temp_dir, "reel_audio.wav")
                clip = AudioFileClip(video_file)
                clip = clip.with_fps(16000)  # Set sample rate
                clip.write_audiofile(
                    audio_file, 
                    codec="pcm_s16le", 
                    ffmpeg_params=["-ac", "1"],
                    logger=None
                )
                clip.close()
                
                # Step 3: Load Whisper model
                status_text.text("🤖 Loading Whisper model...")
                progress_bar.progress(60)
                
                @st.cache_resource
                def load_whisper_model():
                    return whisper.load_model("base")
                
                model = load_whisper_model()
                
                # Step 4: Transcribe
                status_text.text("✍️ Transcribing audio...")
                progress_bar.progress(80)
                
                result = model.transcribe(audio_file)
                transcript = result["text"]
                
                # Step 5: Complete
                status_text.text("✅ Transcription complete!")
                progress_bar.progress(100)
                
                # Display results
                st.success("🎉 Transcript generated successfully!")
                
                # Show transcript
                st.header("📄 Transcript")
                st.text_area(
                    "Generated Transcript:",
                    value=transcript,
                    height=300,
                    help="You can copy this text by selecting all and copying"
                )
                
                # Download button
                st.download_button(
                    label="📥 Download Transcript",
                    data=transcript,
                    file_name="instagram_reel_transcript.txt",
                    mime="text/plain"
                )
                
                # Clear progress indicators
                progress_bar.empty()
                status_text.empty()
        
        except Exception as e:
            error_msg = str(e).lower()
            if "rate-limit" in error_msg or "login required" in error_msg:
                st.error("🚫 **Instagram Rate Limit Reached**")
                st.markdown("""
                **Try these solutions:**
                1. Wait a few minutes and try again
                2. Try a different Instagram Reel URL
                3. Use YouTube Shorts or TikTok instead
                4. Make sure the Instagram account is public
                """)
            elif "private" in error_msg or "not available" in error_msg:
                st.error("🔒 **Content Not Available**")
                st.markdown("This content might be private or removed. Try a public Instagram Reel.")
            else:
                st.error(f"❌ An error occurred: {str(e)}")
                st.markdown("**Possible issues:**")
                st.markdown("- Video URL is invalid or private")
                st.markdown("- Network connection issues")
                st.markdown("- Platform restrictions")
            progress_bar.empty()
            status_text.empty()

# Footer
st.markdown("---")
st.markdown(
    "💡 **MindScrole V1.1** - Built with ❤️ using Streamlit | "
    "Contact: mindscrole@gmail.com"
)
