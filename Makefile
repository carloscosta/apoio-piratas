
build:
	/bin/rm -Rf --verbose ./build/*
	/usr/local/bin/luapress --no-cache

.PHONY: build
