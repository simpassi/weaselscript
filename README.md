# Weaselscript
Encode and decode files to seemingly random weasel hissing noises.

# Usage:
python weaselscript.py <input file>  
```
> echo "Hello" >myfile
> python weaselscript.py myfile
Weasel: ssh sk sss hsk sshk ssh shhh hsk sss﻿sss sss shhh!
> python weaselscript.py myfile
Weasel: ssh hiss ssh sss hiss hissss ss shhh shhh﻿sss sss shhh!
> python weaselscript.py myfile
Weasel: hiss hissss hsk hissss ssh sk ss shhh ss﻿sshk sss sss!
> python weaselscript.py myfile >myfile.weasel
> python weaselscript.py myfile.weasel
Hello
```

# How does it work?
Weasels are clever, so obviously it's not the hissing noises that matter. After all, they change every time you generate the weasel script.

As much fun as it would be to leave it for you to figure out, truth is "ain't nobody got time for that" so here's how it works:
* Each byte of the binary input data is turned into two 4-bit values
* These two values are looked up from an array "weasel_bits" which contains 16 different Unicode space characters
* Two weasel hisses are randomly picked from the array "weasel_hisses" to accompany these spaces

When encoding, the file is prefixed with "Weasel:" and if that sequence is found at the beginning of a file, the above process is turned upside down.

# Why?
The weasels haven't divulged any details of their objectives when it comes to weasel script.
