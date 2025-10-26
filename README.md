# 🎧 CratesAI Pro — macOS DJ Library Analyzer & Organizer

## 🧠 Overview
CratesAI Pro is a macOS desktop app built with **Python 3.11 + PySide6 (Qt)** that helps DJs analyze and organize local music libraries with **BPM, Key (Camelot), Energy, Auto Cues, Smart Crates, Mashup Ideas, and Serato/Traktor exports** — all through a clean, customizable GUI.

No downloading, ripping, or DRM bypass is allowed — the app only analyzes local files the user owns. Discovery pages for Spotify & SoundCloud are **read-only** for browsing/metadata via official APIs.

---

## 🚀 Core Features

### 1. Analyze & Organize
- Folder picker + drag-drop
- Analyze local audio (MP3, M4A, WAV, FLAC, AIFF, OGG)
- Compute:
  - **BPM** (auto-correct <80 ×2, >180 ÷2)
  - **Musical Key** → Camelot (1A–12A / 1B–12B)
  - **Energy** (LUFS 0–10)
  - **Auto Cue Points**: Intro / Drop / Chorus / Outro
- Organizer: copy/move to `Destination/Genre/Artist - Title.ext`
- Genre normalization (robust regex mapping)
- Option to write tags (BPM, Key, Camelot, Genre)

### 2. Smart Crates
- Generates `.m3u8` playlists by:
  - Genre
  - Camelot / Key
  - BPM ranges (configurable)
  - Energy tiers
  - Club Flow (Warmup, Peak, Afterhours)
  - Combo (Genre + Key + BPM)
- Opens crates folder in Finder

### 3. Mashup Ideas
- Suggests compatible tracks using:
  - Camelot adjacency or relative key
  - BPM ±1–2 (half/double handled)
  - Energy ±1–2
- Exports matches as CSV or new M3U crate

### 4. Exports
- **Serato-friendly** JSON & CSV (universal, no DB writes)
- Rekordbox/Traktor via `.m3u8` crates

### 5. Discovery (Read-only)
- Embedded **Spotify** & **SoundCloud** webviews
- Toolbar: Back / Forward / Reload / Close “X”
- Optional metadata lookup via API keys (no audio download)

### 6. Settings
- Stored in `~/CratesAIPro/app/config/settings.yaml`
- Edit defaults for:
  - Library folder, max analysis time
  - Organizer mode (copy/move)
  - Crate BPM buckets & club flow
  - Discovery API credentials
  - Theme (preset/custom)

### 7. Themes
- 4 built-in presets:
  - Dark Violet
  - Neon Blue
  - Sunrise
  - High Contrast
- Live color/font customization
- Persistent via YAML

---

## 🧩 Stack

| Layer | Tech |
|-------|------|
| GUI | PySide6 (Qt) |
| DSP | librosa, numpy, scipy, numba, resampy, pyloudnorm |
| Metadata | mutagen |
| Config | YAML |
| Packaging | PyInstaller (.app bundle) |
| OS | macOS 13+ Apple Silicon |

---

## ⚙️ Folder Structure

