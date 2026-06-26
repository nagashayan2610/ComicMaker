from PIL import Image

def build_comic_page_from_images(images, output_path):

    if not images:
        return

    width = 2000

    # dynamic height based on number of panels
    height = 900 * len(images)

    page = Image.new("RGB", (width, height), "white")

    y = 0

    for img in images:

        img = img.resize((1800, 850))

        page.paste(img, (100, y))
        y += 900

    page.save(output_path)