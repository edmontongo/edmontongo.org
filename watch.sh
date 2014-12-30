reflex -r '\.(sass|scss)$' -- sh -c 'sassc sass/all.sass static/assets/all.css --style compressed' &
hugo server -D --watch && fg
