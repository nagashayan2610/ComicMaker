from PIL import ImageDraw, ImageFont


class StoryboardPanel:

    def __init__(self, image):
        self.image = image
        self.draw = ImageDraw.Draw(self.image)

    def add_dialogue(self, character, text):

        try:
            font = ImageFont.truetype(
                "/System/Library/Fonts/Supplemental/Arial.ttf",
                24
            )
        except:
            font = ImageFont.load_default()

        bubble_x1 = 40
        bubble_y1 = 40
        bubble_x2 = 900
        bubble_y2 = 180

        self.draw.rounded_rectangle(
            [bubble_x1, bubble_y1, bubble_x2, bubble_y2],
            radius=20,
            fill="white",
            outline="black",
            width=4
        )

        dialogue = f"{character}\n\n{text}"

        self.draw.text(
            (70, 70),
            dialogue,
            fill="black",
            font=font
        )

    def save(self, filename):
        self.image.save(filename)