## 2026-01-02 — Phase 3 Started (Mobile Share Ingestion)

### Objective
Design a safe, scalable, and user-native ingestion mechanism to capture Instagram Reel links without scraping, private APIs, or automation risks.

### Key Decision
Shifted from:
- Instagram CLI
- instagrapi / private API automation
- browser scraping & extensions

➡️ **To a mobile-first Android Share Sheet architecture**

This aligns with real user behavior (Instagram is primarily mobile) and avoids all Instagram ToS and stability risks.

---

### Implementation
- Created Android app: **MindscroleShare**
- Registered intent filter for:
  - `android.intent.action.SEND`
  - MIME type: `text/plain`
- App appears in Android system Share Sheet
- Handles shared text via `Intent.EXTRA_TEXT`

---

### Validation
✅ Successfully shared an Instagram Reel from the Instagram Android app  
✅ MindscroleShare app opened via Share Sheet  
✅ Reel URL captured and displayed correctly  

Example captured URL: https://www.instagram.com/reel/DRZefGKX02/?utm_source=ig_web_button_native_share


---

### Why This Architecture Is Correct
- No scraping
- No private APIs
- No automation detection
- Fully user-initiated
- OS-level permission model
- Instagram cannot block or rate-limit this flow

This becomes the **primary ingestion entry point** for Mindscrole.

---

### Current Status
- Android emulator running locally for rapid iteration
- Share Sheet ingestion loop proven end-to-end
- Backend pipeline (Ubuntu + Whisper) already validated in Phase 2

---

### Next Steps (Phase 3 Continuation)
1. Detect and validate Instagram Reel URLs in-app
2. Add explicit UI feedback (“Reel detected ✅”)
3. Add user-controlled action to forward URL to backend pipeline
4. Connect Android app → Ubuntu service (local or remote)

---

### Strategic Note
Mobile Share Sheet ingestion replaces all previous plans involving:
- CLI-based Instagram access
- instagrapi automation
- Selenium / browser scraping

This marks a **major architectural pivot** in favor of stability, safety, and real-world usability.


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
