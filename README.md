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
