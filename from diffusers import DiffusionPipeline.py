from diffusers import DiffusionPipeline
from torch import autocast
import torch

pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype="auto", use_safetensors=True, variant="fp16")

device = 'cuda' if torch.cuda.is_available() else 'cpu'

pipe = pipe.to(device)

prompt = "a photo of an astronaut riding a horse on mars"
with autocast("cpu"):
    # image = pipe(prompt).images[0]
    image = pipe(prompt, guidance_scale=7.5)

# prompt = "An astronaut riding a green horse"

# images = pipe(prompt=prompt).images[0]
image.save(prompt+".png")

print(torch.__version__)