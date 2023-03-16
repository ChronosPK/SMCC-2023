## Solve:

### What is this all about?
- **`Stars`** is a reference to the yellow dots in the pages of the pdf.
- Those patterns represent the [MIC (Machine Identification Code)](https://en.wikipedia.org/wiki/Machine_Identification_Code), <br>
  also known as printer steganography, yellow dots and so on. <br>
  <br>
  ![image](https://user-images.githubusercontent.com/93029180/209968190-a1163d92-6f03-47c7-a9a4-ef62139fec0c.png)
- Tiny dots are embedded on printouts by modern printers. <br>
  Markings like these were used to trace [NSA documents leaked to The Intercept by Reality Winner](https://www.bbc.com/future/article/20170607-why-printers-add-secret-tracking-dots).

- You should search for an online tool 

<br>

### Find tool and decode

- Find [this](https://github.com/dfd-tud/deda) tool used to create custom stars
- Each page hides a letter of the flag
- What elements can we analyze in order to decode? - 
  - looking at each page, we see that the **`serial information`** differs, so we try to extract it
- In each seerial number we haev the unicode value of characters

<br>

- I created a "one-liner" to do the job:
```bash
pdftoppm merged.pdf scan -png; for x in {1..26}; do echo -n $(python3 -c "print(chr($(deda_parse_print $x.png | grep serial | cut -d '-' -f2 | sed 's/^0*//')))"); done
```

<br><br>

## Flag:
`flag{the_new_guy_is_weird}`
