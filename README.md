# ASReview Wide Doc2Vec


[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5084877.svg)](https://doi.org/10.5281/zenodo.5084877)

This repository contains a plugin for [ASReview](https://github.com/asreview) ![logo](https://raw.githubusercontent.com/asreview/asreview-artwork/e2e6e5ea58a22077b116b9c3d2a15bc3fea585c7/SVGicons/IconELAS/ELASeyes24px24px.svg "ASReview"). This plugin adds a new feature extractor based on doc2vec with a wider vector. In combination with a [convolutional neural network](https://github.com/JTeijema/asreview-plugin-model-cnn-17-layer) model, that has been shown to outperform classical algorithms in some situations.


## License
Apache-2.0 License 

## Getting started

Install the new extractor with:

```bash
pip install .
```
from the download folder or run the follow to install directly

```bash
python -m pip install git+https://github.com/JTeijema/asreview-plugin-wide-doc2vec.git
```

## Usage
The new feature extractor can be used with `-e wide_doc2vec`:

```bash
asreview simulate benchmark:van_de_Schoot_2017 -m nn-2-layer -e wide_doc2vec
```

## License
Apache-2.0 License 
