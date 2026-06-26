import re

def parse_script(filepath):

    with open(filepath, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f]

    data = []
    scene = "UNKNOWN"
    current_character = None

    ignore_block = False

    for line in lines:

        # IGNORE TRIPLE QUOTES BLOCK
        if '"""' in line:
            ignore_block = not ignore_block
            continue

        if ignore_block:
            continue

        # skip empty lines
        if not line:
            continue

        # SCENE DETECTION
        if re.match(r"^(INT\.|EXT\.)", line):
            scene = line
            continue

        # CHARACTER DETECTION
        if line.isupper() and len(line.split()) <= 3:
            current_character = line
            continue

        # DIALOGUE
        if current_character:
            data.append({
                "scene": scene,
                "character": current_character,
                "text": line
            })

    return data
