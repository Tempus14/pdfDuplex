While scanning with a scanner without a duplex mode, one gets two files (front and back). 
If there are multiple pages, they are also out of order as after scanning the front pages [1,2,3] the stack will be in the order [3,2,1] before entering the scanner for the back page.  
So this small script can combine these two files in the right order.  
The syntax is as follows:  
`python pdfDuplex.pdf front.pdf back.pdf combined.pdf`  
The only requirement is the package PyPDF2.
