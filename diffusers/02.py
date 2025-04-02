from mflux import Config, Flux1, ModelConfig

QUANTIZATIONS = [None, 3, 4, 6, 8]

if __name__ == "__main__":
    prompt = "Pikachu depicted with elongated features and dramatic chiaroscuro lighting, oil painting texture, in the artistic style of El Greco."

    for quantization in QUANTIZATIONS:
        flux = Flux1(
            model_config=ModelConfig.from_name(
                model_name="Freepik/flux.1-lite-8B", base_model="dev"
            ),
            quantize=quantization,
        )

        image = flux.generate_image(
            seed=25,
            prompt=prompt,
            config=Config(
                num_inference_steps=28,
                guidance=3.5,
                height=1024,
                width=1024,
            ),
        )

        image.save(path=f"freepik_q{quantization}.png", overwrite=True)
