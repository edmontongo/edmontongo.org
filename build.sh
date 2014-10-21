sass --update sass/all.sass:static/assets/all.css --load-path sass/ --force --style compressed
# sassc -o static/assets/all.css -I sass/ -t compressed sass/all.sass
hugo
