.PHONY: watch
watch:
	@hugo server -F --disableFastRender --gc --watch

.PHONY: watchdraft
watchdraft:
	@hugo server -D -F --disableFastRender --gc --watch

.PHONY: build
build:
	@BURL="https://edmontongo.org"; \
	echo "$${BURL}"; \
	export HUGO_ENVIRONMENT="production"; \
	export HUGO_ENV="production"; \
	hugo --gc --minify -F -b "$${BURL}"
