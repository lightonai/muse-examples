# <img src="https://muse.lighton.ai/img/logo.ed57408e.png" width=50/> Examples for the Language Models in Muse.

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)  [![Twitter](https://img.shields.io/twitter/follow/LightOnIO?style=social)](https://twitter.com/LightOnIO)

This repository contains examples for the models in [Muse](https://muse.lighton.ai/), which is currently in public beta.

## Adding an example

To add an example, you should add an entry to the `examples.json` file. You can do so by forking this repository, adding your example and then opening a Pull Request. The format for each individual example is:

```
{
    "title": "A title for your example",
    "color": "a color for your example",
    "sandboxHeader": "A short description",
    "sampleResponse": "A sample of a response of the model", 
    "tags": ["one or more comma-separated tags like `text-generation`"],
    "img": "a link to an image",
    "description": "A longer description",
    "model": "the model",
    "request": {"text": "The input prompt",
                "params": {
                    "mode": "nucleus",
                    "n_tokens": 50,
                    "p": 0.9,
                    ...
                    }
                }
}
```
