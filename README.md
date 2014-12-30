Edmonton Go
===========

This is the content for the Edmonton Go web site.

[![Circle CI](https://circleci.com/gh/edmontongo/edmontongo.org.svg?style=svg)](https://circleci.com/gh/edmontongo/edmontongo.org)

### Setup

* Install the `hugo` binary, download it at [gohugo.io](http://gohugo.io/).
* Install [sassc](https://github.com/sass/sassc).
  Mac: `brew install sassc`

### Deployment

CircleCI automatically deploys the website when changes are merged to master. It takes about 20 seconds to deploy.

* [origin.edmontongo.org](http://origin.edmontongo.org/) is a website endpoint on Amazon S3.
* [edmontongo.org](https://edmontongo.org/) is edge-cached on Amazon CloudFront and secured with SNI. It doesn't update immediately.

### License

See LICENSE.

Webicons by Adam Fairhead, [Fairhead Creative](http://fairheadcreative.com/).
