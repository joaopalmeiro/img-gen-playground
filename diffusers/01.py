from mflux import Config, Flux1

QUANTIZATIONS = [None, 3, 4, 6, 8]

if __name__ == "__main__":
    # prompt = "Pikachu painted by El Greco."
    # prompt = "Pikachu rendered in the style of El Greco."
    prompt = "Pikachu depicted with elongated features and dramatic chiaroscuro lighting, oil painting texture, in the artistic style of El Greco."

    for quantization in QUANTIZATIONS:
        flux = Flux1.from_name(
            model_name="schnell",
            quantize=quantization,
        )

        image = flux.generate_image(
            seed=25,
            prompt=prompt,
            config=Config(
                num_inference_steps=2,
                height=1024,
                width=1024,
            ),
        )

        image.save(path=f"q{quantization}.png", overwrite=True)
