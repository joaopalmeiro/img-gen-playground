# https://www.linkedin.com/posts/huggingface_diffusers-070-is-out-to-bring-you-activity-6994006912719544320-HpwB
# https://huggingface.co/docs/diffusers/optimization/mps
# https://github.com/huggingface/diffusers/releases/tag/v0.7.0
# https://github.com/huggingface/diffusers#text-to-image-generation-with-stable-diffusion
# https://github.com/huggingface/diffusers#running-the-model-locally (+ `brew install git-lfs`)

# https://github.com/huggingface/diffusers/blob/v0.7.0/src/diffusers/utils/import_utils.py#L108
# https://github.com/huggingface/diffusers/blob/v0.7.0/src/diffusers/utils/import_utils.py#L196
# https://github.com/huggingface/diffusers/blob/v0.7.0/src/diffusers/utils/import_utils.py#L265

# https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion#diffusers.StableDiffusionPipeline
# https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion#diffusers.StableDiffusionPipeline.__call__
# https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion#diffusers.pipelines.stable_diffusion.StableDiffusionPipelineOutput

from diffusers import StableDiffusionPipeline
from datetime import datetime

DEFAULT_SIZE: int = 512
DEFAULT_STEPS: int = 50

INSTAGRAM_STORIES_AR: float = 9 / 16

if __name__ == "__main__":
    # https://huggingface.co/runwayml/stable-diffusion-v1-5
    # https://huggingface.co/spaces/CompVis/stable-diffusion-license
    pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")

    # Prepare the pipeline for macOS
    pipe = pipe.to("mps")
    # Recommended if RAM < 64 GB
    pipe.enable_attention_slicing()

    prompt = "Pikachu painted by El Greco."
    prefix = "pikachu"

    n_steps = DEFAULT_STEPS
    # n_steps = 100

    story_width = int(DEFAULT_SIZE * INSTAGRAM_STORIES_AR)

    # First-time "warmup" pass
    # Note: If you change any of the parameters for the output, change them here too (like height and width, for example).
    _ = pipe(prompt, num_inference_steps=1, height=DEFAULT_SIZE, width=story_width)

    # https://stackoverflow.com/a/1186422
    # https://www.canva.com/sizes/instagram/
    output = pipe(
        prompt, num_inference_steps=n_steps, height=DEFAULT_SIZE, width=story_width
    )

    image = output.images[0]
    # https://stackoverflow.com/questions/16755394/what-is-the-easiest-way-to-get-current-gmt-time-in-unix-timestamp-format
    image.save(f"output/{prefix}_{int(datetime.now().timestamp())}.png")
