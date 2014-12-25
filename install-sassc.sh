set -x
set -e

# sassc (3.0.2)

pwd
mkdir -p ./bin $HOME/src/github.com/sass
cd $HOME/src/github.com/sass

git clone --recursive https://github.com/sass/libsass.git -b 3.0.2
git clone https://github.com/sass/sassc.git -b 3.0.2

cd sassc
SASS_LIBSASS_PATH=$HOME/src/github.com/sass/libsass make

# cp $HOME/src/github.com/sass/sassc/bin/sassc ./bin/sassc
