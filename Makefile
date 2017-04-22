
GOLANG = $(shell /usr/bin/which go)
TARGET = ./apoio.server
SOURCE = $(wildcard *.go)

build:
	$(GOLANG) build -x -o $(TARGET) $(SOURCE)

clean:
	rm --verbose $(TARGET) *.log

.PHONY: clean
