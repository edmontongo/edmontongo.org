Edmonton Go
===========

This is the content for the Edmonton Go web site.

[![Circle CI](https://circleci.com/gh/edmontongo/edmontongo.org.svg?style=svg)](https://circleci.com/gh/edmontongo/edmontongo.org)

### Setup

* Install the `hugo` binary, download it at [gohugo.io](http://gohugo.io/).
* Install [sassc](https://github.com/sass/sassc).
  Mac: `brew install sassc`
* SassC doesn't watch for file changes, but you can use [Reflex](https://github.com/cespare/reflex).

### Deployment

CircleCI automatically deploys the website when changes are merged to master. It takes about 20 seconds to deploy.

* [edmontongo.org.s3-website-us-east-1.amazonaws.com](http://edmontongo.org.s3-website-us-east-1.amazonaws.com/) is a website endpoint on Amazon S3.
* [edmontongo.org](https://edmontongo.org/) is cached on CloudFlare with Flexible SSL enabled.

### License

See LICENSE.

Webicons by Adam Fairhead, [Fairhead Creative](http://fairheadcreative.com/).
