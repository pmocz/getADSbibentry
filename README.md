# getADSbibentry
quickly grab ADS bibtex entries for your latex bibtext bibliography from the ADS article tag

# usage

```python
getADSbibentry.py <>
```

# example

Add to your .bashrc the alias
```bash
alias getbib="python <path to python script>/getADSbibentry.py"
```

Then, in the console, do:
```console
getbib "2019PhRvL.123n1301M,2019ApJ...884L..35M" > mybib.bib
```

To obtain a text file **mybib.bib**:
```
@ARTICLE{2019PhRvL.123n1301M,
       author = {{Mocz}, Philip and {Fialkov}, Anastasia and {Vogelsberger}, Mark and
         {Becerra}, Fernando and {Amin}, Mustafa A. and {Bose}, Sownak and
         {Boylan-Kolchin}, Michael and {Chavanis}, Pierre-Henri and
         {Hernquist}, Lars and {Lancaster}, Lachlan and {Marinacci}, Federico and
         {Robles}, Victor H. and {Zavala}, Jes{\'u}s},
        title = "{First Star-Forming Structures in Fuzzy Cosmic Filaments}",
      journal = {\prl},
     keywords = {Astrophysics - Astrophysics of Galaxies, Astrophysics - Cosmology and Nongalactic Astrophysics, General Relativity and Quantum Cosmology},
         year = "2019",
        month = "Oct",
       volume = {123},
       number = {14},
          eid = {141301},
        pages = {141301},
          doi = {10.1103/PhysRevLett.123.141301},
archivePrefix = {arXiv},
       eprint = {1910.01653},
 primaryClass = {astro-ph.GA},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2019PhRvL.123n1301M},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}

@ARTICLE{2019ApJ...884L..35M,
       author = {{Mocz}, Philip and {Burkhart}, Blakesley},
        title = "{A Markov Model for Non-lognormal Density Distributions in Compressive Isothermal Turbulence}",
      journal = {\apjl},
     keywords = {Star formation, Interstellar medium, Astrophysics - Astrophysics of Galaxies},
         year = "2019",
        month = "Oct",
       volume = {884},
       number = {2},
          eid = {L35},
        pages = {L35},
          doi = {10.3847/2041-8213/ab48f6},
archivePrefix = {arXiv},
       eprint = {1908.00544},
 primaryClass = {astro-ph.GA},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2019ApJ...884L..35M},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
```

