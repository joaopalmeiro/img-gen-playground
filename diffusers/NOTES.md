# Notes

- https://github.com/joaopalmeiro/template-python-uv-script
- https://www.pruna.ai/blog/quantization-for-image-generation
- https://huggingface.co/Freepik/flux.1-lite-8B
- https://huggingface.co/docs/diffusers/optimization/mps
- https://github.com/PrunaAI/pruna?tab=readme-ov-file#-algorithm-overview
- https://docs.pruna.ai/en/stable/setup/pip.html:
  - "pruna is officially supported on Linux."
- https://github.com/AutoGPTQ/AutoGPTQ/issues/535
- https://github.com/huggingface/diffusers/blob/v0.32.2/docs/source/en/quantization/bitsandbytes.md
- https://huggingface.co/docs/bitsandbytes/main/en/installation: "bitsandbytes does not yet support Apple Silicon / Metal with a dedicated backend."

## Commands

```bash
deactivate && uv venv --seed && source .venv/bin/activate && uv pip install -r requirements.txt
```

```bash
uv venv && source .venv/bin/activate && uv pip install -r requirements.txt
```

### Clean slate

```bash
rm -rf .mypy_cache/ .ruff_cache/ .venv/
```
