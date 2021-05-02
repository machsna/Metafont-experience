# Excercise 1.10

Once the interactive input has been made, you can convenientaly access it again
by editing the LOG file. Just comment out the start and end messages and delete
the leading \* characters.

On-liner for executing the MF file:

```
for a in A.mf ; do gf=${a/\.mf/.2602gf} ; dvi=${a/\.mf/.dvi} ; gftodvi "$gf" ; xdg-open "$dvi" &> /dev/null ; done
```
