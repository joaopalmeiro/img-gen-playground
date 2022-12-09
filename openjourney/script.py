import time
import urllib.request

import replicate
from dotenv import load_dotenv
from slugify import slugify

load_dotenv()

PROMPT_PREFIX: str = "mdjrny-v4 style"
SIZE: int = 512
NUM_INFERENCE_STEPS: int = 50
SEED: int = 2

PROMPT: str = (
    f"{PROMPT_PREFIX} portrait of charizard, elegant, highly detailed, digital painting"
)

if __name__ == "__main__":
    # https://replicate.com/prompthero/openjourney/versions
    # https://replicate.com/prompthero/openjourney/api
    model = replicate.models.get("prompthero/openjourney")
    version = model.versions.get(
        "9936c2001faa2194a261c01381f90e65261879985476014a0a37a334593a05eb"
    )
    output = version.predict(
        prompt=PROMPT,
        width=SIZE,
        height=SIZE,
        num_outputs=1,
        num_inference_steps=NUM_INFERENCE_STEPS,
        guidance_scale=7,
        seed=SEED,
    )

    print("URL:", output[0])
    urllib.request.urlretrieve(
        output[0], f"output/{slugify(PROMPT)}-{int(time.time())}.png"
    )
