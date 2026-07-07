# Automated Background Remover (Computer Vision Pipeline)

An AI-powered computer vision utility developed in Python to automatically upscale images and remove complex backgrounds from logos, badges, and structural geometric shapes with high-precision edge retention.
## 🖼️ Visual Preview (Before & After)

| Raw Input (`ax_input`) | Processed Output (`ax_utput`) |
| :---: | :---: |
| <img src="ax_input/%23e9d5ff.png" width="300"> | <img src="ax_utput/logo_transparent.png" width="300"> |
---

## 🛠️ System Overview & Pipeline Architecture

The processing pipeline is completely decoupled and follows a sequential, deterministic flow to eliminate degradation and edge blurring: