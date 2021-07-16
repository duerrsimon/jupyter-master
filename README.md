# EPFL JupyterBook template

This is a preconfigured template to use JupyterBooks at EPFL coupled with the JupyterHub platform at `noto.epfl.ch`. 

You can view a preview [here](https://epfl-data-champions.github.io/EPFL-JupyterBook/intro.html)

## How to use

Install required packages

```
$ pip install -r requirements.txt
```


Then modify the `.md` and `.ipynb` files. 

Modify the `_toc.yml` and `_config.yml` to configure which files to build and to setup latex macros,
book title, footer etc. 



### Build the book

```
jupyter-book build --toc _toc.yml 
```


To change the footer edit the `<a>` tags in `_config.yml`. 

The toc needs to be structured as in order for the styling to work correctly

``` yaml
- file: intro
- part: Chapter Headline 
  chapters:
    - file: markdown
    - file: notebooks

```
