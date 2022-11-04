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

if __name__ == "__main__":
    # https://huggingface.co/runwayml/stable-diffusion-v1-5
    # https://huggingface.co/spaces/CompVis/stable-diffusion-license
    pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")

    # Prepare the pipeline for macOS
    pipe = pipe.to("mps")
    # Recommended if RAM < 64 GB
    pipe.enable_attention_slicing()

    prompt = "Pikachu painted by El Greco."

    n_steps = 50  # Default
    # n_steps = 100

    # First-time "warmup" pass
    _ = pipe(prompt, num_inference_steps=1)

    output = pipe(prompt, num_inference_steps=n_steps)

    image = output.images[0]
    image.save("pikachu.png")
