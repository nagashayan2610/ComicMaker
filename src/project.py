import os
from parser import parse_script
from ai_generator import generate_comic_panel
from layout import StoryboardPanel
from page_builder import build_comic_page_from_images


# Scene based page builder

def scene_pages(data):

    pages = []
    page = []

    for item in data:

        page.append(item)

        # create page when it becomes visually heavy OR 4 dialogues max
        if len(page) >= 4:
            pages.append(page)
            page = []

    if page:
        pages.append(page)

    return pages



# MAIN PROGRAM

def main():

    script_path = "scripts/scene.txt"

    print(f"📄 Reading script: {script_path}")

    comic_name = input("📖 Comic name: ").strip()

    if not comic_name:
        comic_name = "comic"

    comic_name = comic_name.replace(" ", "_")

    data = parse_script(script_path)

    print(f"✅ Total dialogues parsed: {len(data)}")

    if len(data) == 0:
        print("❌ No data found. Check your scene.txt format.")
        return

    os.makedirs("output", exist_ok=True)

    pages = scene_pages(data)

    print(f"📚 Total pages to generate: {len(pages)}")

    page_num = 1

    for page_data in pages:

        print(f"\n🎬 Generating Page {page_num}")

        images = []

        panel_num = 1

        for item in page_data:

            print(f"   🧩 Panel {panel_num} - {item['character']}")

            img = generate_comic_panel(
                item["scene"],
                item["character"],
                item["text"]
            )

            panel = StoryboardPanel(img)
            panel.add_dialogue(item["character"], item["text"])

            images.append(panel.image)

            panel_num += 1

        output_path = f"output/{comic_name}_{page_num}.png"

        build_comic_page_from_images(images, output_path)

        print(f"✅ Saved: {output_path}")

        page_num += 1

    print("\n 'cp output/*.png backup/' use this for backup the Comic!!!")
    print("\n 'rm -rf output/*' to remove the output!!!")
    print("\n🎉 CONGRATS YOUR COMIC IS READY BTW!!!")


if __name__ == "__main__":
    main()