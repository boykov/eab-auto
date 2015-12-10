#!/bin/sh

gs -dSAFER -dBATCH -dNOPAUSE -r300x300 -dDITHERPPI=120 -sDEVICE=psmono -sOutputFile=output.ps noname.ps

gs -sDEVICE=psmono  -dNOPAUSE -dQUIET -dBATCH -dPDFSETTINGS=/screen  -dLZWEncodePages=true -dUseFlateCompression=true  -sPAPERSIZE=letter  -sColorConversionStrategy=Mono -dProcessColorModel=/DeviceGray -sOutputFile=output.ps input.pdf &
ps2pdf output.ps output.pdf

convert -density 300x300 -compress jpeg output.pdf -monochrome DitheredOutput.pdf

gs -sDEVICE=pdfwrite -dNOPAUSE -dQUIET -dBATCH -sColorConversionStrategy=Gray -dProcessColorModel=/DeviceGray -sOutputFile=output.pdf input.pdf

gs -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf

gs -sDEVICE=pdfwrite -dNOPAUSE -dQUIET -dBATCH -dPDFSETTINGS=/ebook -sColorConversionStrategy=Mono -dProcessColorModel=/DeviceGray -sOutputFile=output.pdf input.pdf

gs -sDEVICE=pdfwrite -dNOPAUSE -dQUIET -dBATCH -dPDFSETTINGS=/screen -sColorConversionStrategy=Gray -dProcessColorModel=/DeviceGray -sOutputFile=output.pdf input.pdf


gs -sDEVICE=pdfwrite -dNOPAUSE -dQUIET -dBATCH -sColorConversionStrategy=Mono -dProcessColorModel=/DeviceGray -sOutputFile=output.pdf input.pdf
