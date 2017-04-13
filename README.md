# Example HTML Font Sizes

This set of example HTML articles show you how can set and restore font sizes.

This illustrates how you can implement an app where people can choose their desired font sizes.

## Environment

Twixl article-based application

## Packaging the article files

Open a terminal in the root folder and run the following command:

```bash
python package_articles.py .
```

## How does it work?

The core of this example is contained in the ```__SharedResources/font_size.js``` script.

This script contains 3 different functions:

* ```changeFontSize(scale)```: this function allows you to dynamically change the font size. 
The base font size is ```16px``` and the scale is expressed as a percentage of this base size. 
A value of ```100``` means a font size of ```16px```, a value of ```200``` means a font size of ```32px```. 
The line height is also increased automatically and is always ```150%``` of the font size. 
Calling this function automatically saves the font size to HTML local storage using the ```saveFontScale(scale)``` function.

* ```saveFontScale(scale)```: this function saves the font size to HTML local storage so that it can be retrieved later.

* ```restoreFontScale(scale)```: this function is called in every HTML page so correctly set the initial font size.  
If a scale is found in the HTML local storage, that one is used.   
If nothing was persisted before, it sets the correct default font size.

## Caveats

Be careful when choosing the key name which is going to be used for the HTML local storage. The storage is shared
between all applications on the devices, so it's best to prefix it with the application identifier to make the keys
specific to each app you are planning to use this in.

## Used Technologies

* [HTML5 Local Storage](https://en.wikipedia.org/wiki/JavaScript)
* [JavaScript](https://www.javascript.com)
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)