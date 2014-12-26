set -x
set -e
if [ $CIRCLE_BRANCH == 'master' ]; then
  s3up -source=public/ -bucket=edmontongo.org -key=$AWS_ACCESS_KEY_ID -secret=$AWS_SECRET_ACCESS_KEY
fi
