## How to upload Jupyter Lab to Binder


1. Create a repro with your Jupyter Lab
   - add requirements.txt for the project
   - note can only have 1 requirements.txt/repro
1. Go to [binder](https://mybinder.org/)
1. fill out the form
  - *add the relative path to the ipynb file* or the binder points to the files and not the Jupyter Lab
1. copy the url or binder badge and add it the README.md file in the repro.

todos:
howto set up own binder server - cloud?

## How to add/create/modify data:

for example to render a narrative - upload your capstatements and download the results

1. open up the file menu - just like the Git interface
1. download files to save, edit (can always copy and paste too)
1. upload files to use as input data or to modify
1. note size limitations
1. note the data is not saved in the binders and is public

adding fhirclient to Binders

- can't be in parent
- copy in each place locally  :-(
- make a package
