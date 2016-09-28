#!/bin/bash
# Modified from http://echorand.me/presentation-slides-with-jupyter-notebook.html

if (($# != 1))
then
  mess="Slide update"
else
  mess="$1"
fi
jupyter-nbconvert --to slides slides.ipynb --reveal-prefix=reveal.js
mv teachingdemo.slides.html  index.html
mkdir -p /tmp/workspace
cp -r * /tmp/workspace/
git add -A .
git commit -m "$mess"
git checkout -B gh-pages
cp -r /tmp/workspace/* .
git add -A .
git commit -m "$mess"
git push origin master gh-pages
git checkout master
rm -rf /tmp/workspace
