---# ComicMaker #---

An AI-powered comic generator built with Python and Stable Diffusion Turbo that converts screenplay-style scripts into comic book pages automatically.


---# Overview #---

ComicMaker reads a screenplay-style text file, extracts scenes, characters, and dialogue, generates AI illustrations for every dialogue, places speech bubbles on each panel, and
finally combines multiple panels into complete comic pages.

The project demonstrates AI image generation, natural language parsing, image processing, and automated comic layout generation.


---# Features #---

- 🎬 Parse screenplay-style scripts
- 🤖 AI-generated comic panels using Stable Diffusion Turbo
- 💬 Automatic speech bubble generation
- 📄 Automatic comic page creation
- 🖼️ Saves comics as PNG images
- 📚 Supports multi-page comics
- ⚡ Fast image generation using SD-Turbo


---# Technologies Used #---

- Python
- Diffusers
- Stable Diffusion Turbo
- PyTorch
- Pillow (PIL)
- Regular Expressions (re)


---# Project Structure #---

ComicMaker/
│
├── src/
│   ├── project.py
│   ├── parser.py
│   ├── ai_generator.py
│   ├── layout.py
│   └── page_builder.py
│
├── scripts/
│   └── scene.txt
│
├── sample_output/
│
├── requirements.txt
├── README.md
└── .gitignore


---# Usage #---

Place your screenplay inside:

scripts/scene.txt

Run:

python src/project.py

Enter a comic name when prompted.

The generated comic pages will be saved inside the output folder.


---# Script Format #---

Rules:

1. SCENE FORMAT
INT. or EXT. must start scene lines

Example:
INT. ROOFTOP - NIGHT

2. CHARACTER FORMAT
Must be uppercase only

after character is dialogue

Example:
I will save.

3. DIALOGUE FORMAT
Next line

4. COMMENT BLOCK (IGNORED BY SYSTEM)
Anything inside triple quotes is ignored:

5. DO NOT USE:
- colon after character name
- free paragraph writing
- mixed formats

6. RECOMMENDED STYLE:
Keep each dialogue short (1–2 lines)
Each scene = multiple character exchangesxample:
name in uppercase


---# How It Works #---

scene.txt
      │
      ▼
parser.py
      │
      ▼
Extract Scene + Character + Dialogue
      │
      ▼
ai_generator.py
      │
      ▼
Generate AI Comic Panel
      │
      ▼
layout.py
      │
      ▼
Add Speech Bubble
      │
      ▼
page_builder.py
      │
      ▼
Final Comic Page


---# Sample Output #---

Sample comic pages are available inside the >> sample_output/ << folder.


---# Made By #---

--> Nagashayan Alugandula <--

B.Tech Mechanical Engineering  
IIT (ISM) Dhanbad

GitHub:
https://github.com/nagashayan2610


---# ⭐ If you like this project #---

Consider giving the repository a ⭐ on GitHub.

Thank You 😀
