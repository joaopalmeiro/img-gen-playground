# Notes

- https://github.com/joaopalmeiro/template-python-uv-script
- https://huggingface.co/HiDream-ai/HiDream-I1-Fast
- https://huggingface.co/docs/diffusers/optimization/mps
- https://huggingface.co/docs/diffusers/main/en/api/pipelines/hidream
- https://huggingface.co/models?library=diffusers&sort=trending
- https://huggingface.co/models?library=diffusers&sort=downloads
- https://huggingface.co/models?pipeline_tag=text-to-image&library=diffusers&sort=trending
- https://huggingface.co/CompVis/stable-diffusion-v1-4:
  - "resolution 512x512"

## Commands

```bash
deactivate && uv venv && source .venv/bin/activate && uv pip install -r requirements.txt
```

```bash
uv venv && source .venv/bin/activate && uv pip install -r requirements.txt
```

### Clean slate

```bash
rm -rf .mypy_cache/ .ruff_cache/ .venv/
```
