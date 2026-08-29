#!/bin/sh
cd "$(dirname "$0")"
echo "Starting local phishing-awareness simulation..."
echo "Open http://127.0.0.1:8000/index.html in your browser."
python3 -m http.server 8000 --directory web
