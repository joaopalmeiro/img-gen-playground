from diffusers import DiffusionPipeline

if __name__ == "__main__":
    pipe = DiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4").to("mps")
    pipe.enable_attention_slicing()

    prompt = "Pikachu depicted with elongated features and dramatic chiaroscuro lighting, oil painting texture, in the artistic style of El Greco."
    image = pipe(prompt).images[0]

    image.save("example.png")
