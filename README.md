Hide files in PNG
====
Using this script you can hide any file in a PNG image. The script creats a fake chunk and add the file to that chunk which is ignored by PNG processing tools but it can be retrived later.

Requirement
====
Only python 2.7 is required, you can use python3 also just change those "print" statements.

Usage
====
<pre>png_hiding.py <input.png> <payload_file> <output.png> </pre>

Ex:<br>

<pre>python png_hiding.py sample.png png_hiding.py out.png

Start: 16 Count: 1266
[*] Header: IHDR Length: 13 Read_CRC: aa6971de Calc_CRC aa6971de
[*] Header: bKGD Length: 6 Read_CRC: a0bda793 Calc_CRC a0bda793
[*] Header: pHYs Length: 9 Read_CRC: 009a9c18 Calc_CRC 009a9c18
[*] Header: tIME Length: 7 Read_CRC: 71e7cf0a Calc_CRC 71e7cf0a
[*] Header: tEXt Length: 25 Read_CRC: 57810e17 Calc_CRC 57810e17
[*] Header: IDAT Length: 395 Read_CRC: 5130624e Calc_CRC 5130624e
[*] Header: IEND Length: 0 Read_CRC: ae426082 Calc_CRC ae426082
</pre>

We get information like <b>Start</b> and <b>Count</b> which is offset at which our payload is written and no of bytes that are written respectively.

You can retrive the content via several method:

* Using 'dd'
<pre>dd if=out.png of=recovered_file.py bs=1 skip=16 count=1266</pre>

* Using python

You can use this one liner to recover the above file, replace start and Count values to recover your file.
<pre>python -c "open('recovered_file.py','wb').write(open('out.png','rb').read()[16 : 16+1266])"</pre>

You can also use language specific codes to recover the file, just google it for your language.

Final Note
====
This script can be used to fix invalid CRC error of a PNG which you can encounter in CTFs competitions or you can use it to explore different chunks present in a PNG file (just comment out the file writing part).

For increased security you can encrypt file before adding it to the PNG and then decrypt it after recovering.

If any suggestions or request mail me or open a issue.

Author
====
Arun Kumar Shreevastava
