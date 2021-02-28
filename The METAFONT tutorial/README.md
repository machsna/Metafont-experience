# The METAFONT tutorial

Link: [http://metafont.tutorial.free.fr/downloads/mftut.pdf][1]

## Appendix B: Instructions for the Compilation of the _gray_ Font

p. 72: The `mf` code needs quotes:

```
mf '\mode=ljfour; input gray.mf'
```

Stupid mistake while adding the _gray_ font files to `~/texmf`: I put the TFM
files in the same directory as the PK files. That will not work. My stupidity
is now manifest on the internet, cf. [fonts - tfm files in local ~/texmf not
found - TeX - LaTeX Stack Exchange][2].

[1]: http://metafont.tutorial.free.fr/downloads/mftut.pdf
[2]: https://tex.stackexchange.com/questions/585291/tfm-files-in-local-texmf-not-found
