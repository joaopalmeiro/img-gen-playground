# Notes

- https://github.com/joaopalmeiro/template-python-uv-script
- https://www.pruna.ai/blog/quantization-for-image-generation
- https://huggingface.co/Freepik/flux.1-lite-8B
- https://huggingface.co/docs/diffusers/optimization/mps:
  - https://github.com/huggingface/diffusers/issues/9063
  - https://huggingface.co/docs/diffusers/en/optimization/fp16#half-precision-weights
- https://github.com/PrunaAI/pruna?tab=readme-ov-file#-algorithm-overview
- https://docs.pruna.ai/en/stable/setup/pip.html:
  - "pruna is officially supported on Linux."
- https://github.com/AutoGPTQ/AutoGPTQ/issues/535
- https://github.com/huggingface/diffusers/blob/v0.32.2/docs/source/en/quantization/bitsandbytes.md
- https://huggingface.co/docs/bitsandbytes/main/en/installation: "bitsandbytes does not yet support Apple Silicon / Metal with a dedicated backend."
- https://github.com/filipstrand/mflux
- https://huggingface.co/collections/black-forest-labs/flux1-679d013aee236841c0e9d38a
- https://huggingface.co/docs/diffusers/v0.32.2/en/api/pipelines/flux#diffusers.FluxPipeline
- https://github.com/continue-revolution/sd-webui-segment-anything/issues/16
- https://huggingface.co/black-forest-labs/FLUX.1-schnell: "`FLUX.1 [schnell]` can generate high-quality images in only 1 to 4 steps."
- https://github.com/filipstrand/mflux/blob/v.0.6.2/pyproject.toml#L15
- https://huggingface.co/docs/huggingface_hub/en/guides/manage-cache#clean-your-cache
- https://github.com/filipstrand/mflux?tab=readme-ov-file#-current-limitations: "Negative prompts not supported."
- https://github.com/zobweyt/textcase
- https://github.com/AgentOps-AI/tokencost
- https://github.com/filipstrand/mflux?tab=readme-ov-file#-third-party-huggingface-model-support:
  - https://huggingface.co/shuttleai/shuttle-3-diffusion
- https://www.gradii.fun/:
  - `<p style="font-size: 10em;font-weight: 700;letter-spacing: -0.02em;font-family: &quot;Space Mono&quot;;opacity: 1;line-height: 1;color: rgb(241, 241, 241);font-style: normal;text-shadow: rgb(245, 245, 245) 0px 0px 24px;transform: translate(0px, 0px);white-space: pre;text-wrap-style: initial;text-align: center;">Gradii.</p>`
    - `text-shadow: rgb(245, 245, 245) 0px 0px 24px;`

## Commands

```bash
deactivate && uv venv --seed && source .venv/bin/activate && uv pip install -r requirements.txt
```

```bash
uv venv && source .venv/bin/activate && uv pip install -r requirements.txt
```

```bash
huggingface-cli scan-cache
```

```bash
huggingface-cli delete-cache
```

### Clean slate

```bash
rm -rf .mypy_cache/ .ruff_cache/ .venv/
```
