# img-gen-playground

## Development

First of all, install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) (if necessary).

```bash
conda env create -f environment.yml
```

```bash
conda activate img-gen-playground
```

```bash
python pikaichu.py
```

## Notes

- `conda list`
- `conda env remove --name img-gen-playground`
- `black pikaichu.py`
- PikAIchu or pikAIchu
- https://photos.app.goo.gl/NRqNemh8hrtPZVMv8

### Install openpyxl on Windows 10 with Anaconda

- Install the following version of [pywin32](https://github.com/mhammond/pywin32) first: `pip install --user pywin32==228` ([source](https://github.com/conda/conda/issues/11503#issuecomment-1147095405))
- [ImportError: DLL load failed while importing shell: Can not find procedure.](https://github.com/conda/conda/issues/11503) (open) issue
