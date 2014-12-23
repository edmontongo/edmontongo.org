set -x
set -e
if [ ! -e /usr/local/bin/hugo ]; then
  wget https://github.com/spf13/hugo/releases/download/v0.12/hugo_0.12_linux_amd64.tar.gz
  tar xvzf hugo_0.12_linux_amd64.tar.gz
  sudo cp hugo_0.12_linux_amd64/hugo_0.12_linux_amd64 /usr/local/bin/hugo
fi
