# JupyterBook template

This is a preconfigured template to use JupyterBooks with a JupyterHub platform 

You can view a preview [duerrsimon.github.io/jb_clone_public](https://duerrsimon.github.io/jb_clone_public)
The student version is here [duerrsimon/jb_clone_public](https://github.com/duerrsimon/jb_clone_public)

## How to use locally

Install required packages

```
$ pip install -r requirements.txt
```

Then modify the `.md` and `.ipynb` files. 

Modify the `_toc.yml` and `_config.yml` to configure which files to build and to setup latex macros,
book title, footer etc. 



## Use GitHub actions to deploy a student version 

This is the master repository that you can choose to keep private if you want. You need to create a second repository (student version). This one you never edit directly. Instead github actions will populate it whenever you change the master repository (via a Github Action). 

The workflow for deployment of the student repository is `.github/workflows/.publish.yml` (configuration in `.publish/recipe.yml`). 
The action used is [duerrsimon/repo_selective_sync_remove_solutions v1.0.0](https://github.com/duerrsimon/repo_selective_sync_remove_solutions)
This workflow will copy all files to student version (except for the ones that you specify in the recipe to be removed). Additionally, all notebook cells tagged `solution` will be removed. 

![How to tag cells](https://jupyterbook.org/_images/tags_notebook.png)

If you only want to use the workflow that copies the files to a public student version only use `.github/workflows/.publish.yml`. 

If you want to build the teacher and student JupyterBooks and deploy them check `.github/workflows/build-book.yml` (teacher version) and `build-book.yml` (student version). The student action is copied into the public student repo into the `.github/workflows/` folder and therefore only executed there. 

Check [JupyterBook](https://jupyterbook.org) page for more details. You can use different configurations for student and teacher version. 


For the workflow to work you need to create a Personal Access Token and add it as secret to the master repository (`TARGET_PAT`)

## Deploy private teacher version to any web destination
Github does not offer a private version of GitHub pages.  By default therefore the teacher jupyterbook is built but not published somewhere (you can download it from the artefact page)

If you want to host the solutions somewhere you can uncomment the commented sections in `.github/workflows/build-book.yml` to deploy the website files via rsync to any SSH host (after setting up a private key and other required secrets). 




