## 2025-12-27 — Phase 2.7 Decision (Instagram Automation Pivot)

### Context
Multiple experiments were conducted to evaluate automated ingestion of Instagram Reels via:
- CLI tools
- Private APIs (instagrapi)
- Reverse-engineered approaches

All private API–based methods were either blocked at the environment/IP level or deemed high-risk and non-viable for a product-facing MVP.

### Key Finding
Instagram actively restricts:
- Programmatic login from server/Linux environments
- Private API access
- DM-based automation

This makes backend-driven Instagram automation unreliable and unsafe.

### Decision
Mindscrole will **not** automate Instagram ingestion via:
- DMs
- Private APIs
- Scraping
- Background services

Instead, ingestion will move to a **user-initiated browser extension model**.

### New Ingestion Model (Approved)
- User logs into Instagram normally (browser/app).
- A developer-mode browser extension:
  - reads the current page URL (e.g. `/reel/{id}`)
  - performs no background scraping.
- The reel URL is sent to the Mindscrole pipeline **only when the user explicitly triggers the action** (click / command).

### Rationale
- Zero ToS violation
- No account risk
- Deterministic behavior
- Clear user intent
- Scalable and future-proof

### Status
- Instagram private API approaches permanently abandoned.
- Browser extension ingestion approved as the safe automation path.
- Proceeding to extension design and schema integration.

## 2025-12-27 — Phase 2 Complete (Transcription Pipeline)

### Completed
- Implemented end-to-end transcription pipeline:
  - Instagram Reel URL → audio extraction (yt-dlp)
  - Audio conversion to WAV (ffmpeg)
  - Local transcription using OpenAI Whisper
  - Transcript saved to `data/transcripts/`
- Pipeline tested successfully on Ubuntu (32 GB RAM)

### GPU / CUDA Decision
- System GPU: NVIDIA GeForce MX350 (CUDA capability 6.1)
- PyTorch build supports CUDA >= 7.0
- Attempting GPU execution caused runtime CUDA kernel errors
- Decision: **Force Whisper to run on CPU**
  - `whisper.load_model("small", device="cpu")`
  - Stable, reproducible, and sufficient for short-form content
- CPU-based Whisper chosen as default for Phase 2 MVP

### Environment Notes
- Python 3.12
- Virtual environment required due to PEP 668 (externally managed system Python)
- yt-dlp and whisper installed inside project `venv`
- ffmpeg available system-wide

### Status
- Phase 2 (audio → transcript) is **stable and complete**
- Ready to proceed to Phase 3 (structuring, prioritization, and metadata)
## 2025-12-27 — Phase 1 Complete (Project Foundation)

### Objective
Establish a clean, reproducible project foundation before building the AI pipeline.

### Completed
- Initialized GitHub repository (`mindscrole`)
- Standardized project structure:
