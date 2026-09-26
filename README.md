# AURA-X Blockchain Demo — Render Free Ready

Educational Flask + Docker blockchain demonstration with a simple browser dashboard.

## Local run
`python -m pip install -r requirements.txt`

Windows: `set PORT=8000 && python app.py`

Open `http://127.0.0.1:8000`

## Render
1. Upload this folder to a GitHub repository.
2. In Render choose **New → Web Service** and select the repository.
3. Runtime: **Docker**.
4. Plan: **Free** (if offered on your account/service).
5. Branch: `main`.
6. Root Directory: blank when these files are at repository root.
7. Deploy.

The app reads Render's `PORT` environment variable and binds to `0.0.0.0`.

## Important
This is an educational blockchain demo. It does not implement Bitcoin consensus, wallets, cryptographic signatures, peer-to-peer networking, a real token, or real monetary value.
