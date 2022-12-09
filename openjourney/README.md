# openjourney

> Stable Diffusion fine-tuned on Midjourney v4 images

## Development

- `pipenv install --python 3.7`
- `pipenv run python script.py`
- `pipenv run isort --profile black script.py && pipenv run black script.py`

## References

- https://replicate.com/prompthero/openjourney
- https://github.com/replicate/replicate-python

## Notes

- Default prompt: `mdjrny-v4 style portrait of female elf, intricate, elegant, highly detailed, digital painting, artstation, concept art, smooth, sharp focus, illustration, art by artgerm and greg rutkowski and alphonse mucha, 8k`
- First try (`out-0.png`):
  - `prompt`: mdjrny-v4 style portrait of pikachu, elegant, highly detailed, digital painting
  - `width` and `height`: 512
  - `num_outputs`: 1
  - `num_inference_steps`: 50
  - `guidance_scale`: 7
  - `seed`: 2
- `pipenv install black isort replicate python-dotenv python-slugify`
