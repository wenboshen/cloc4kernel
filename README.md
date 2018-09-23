# cloc4kernel

### How to use
1. build kernel source code
2. copy `cloc4kernel.py` to kernel source root directory
3. run script, it will generate a folder at ../cloc
```
python cloc4kernel.py
```
4. go to ../cloc, run `cloc .` to count lines of code

### How cloc4kernel works
1. cloc4kernel requires kernel to be compiled
2. According to the generated .o file, it will find and copy all 
corresponding c and assembly files to ../cloc
3. It will grep all c and assembly files to find all headers and copy
all headers to ../cloc
