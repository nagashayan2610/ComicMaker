from diffusers import AutoPipelineForText2Image
import torch

pipe = AutoPipelineForText2Image.from_pretrained(
    "stabilityai/sd-turbo",
    torch_dtype=torch.float16,
    variant="fp16"
)

pipe = pipe.to("mps" if torch.backends.mps.is_available() else "cpu")


def generate_comic_panel(scene, character, dialogue):

    prompt = f"""
    Marvel comic book style illustration.

    cinematic lighting,
    ultra detailed,
    dramatic framing,
    graphic novel art,
    professional inked comic style,

    CHARACTER CONSISTENCY:
    {character} is a consistent superhero character, same outfit, same face style across panels.

    SCENE:
    {scene}

    DIALOGUE MOMENT:
    {dialogue}

    high contrast, dynamic composition, movie still style
    """

    image = pipe(
        prompt,
        num_inference_steps=1,
        guidance_scale=0.0
    ).images[0]

    return image