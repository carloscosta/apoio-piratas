
build:
	/bin/mkdir -p --verbose inc
	/bin/mkdir -p --verbose posts
	/bin/rm -Rf --verbose ./build/*
	/usr/local/bin/luapress --no-cache

.PHONY: build
