set -x
set -e

# sassc (3.0.2)

export SASS_BUILD_DIR=$HOME/src/github.com/sass

mkdir -p $CIRCLE_BUILD_DIR/bin $HOME/src/github.com/sass

cd $HOME/src/github.com/sass
git clone --recursive https://github.com/sass/libsass.git -b 3.0.2
git clone https://github.com/sass/sassc.git -b 3.0.2

cd sassc
SASS_LIBSASS_PATH=$HOME/src/github.com/sass/libsass make

cp $HOME/src/github.com/sass/sassc/bin/sassc $CIRCLE_BUILD_DIR/bin/sassc

echo $SASS_BUILD_DIR
