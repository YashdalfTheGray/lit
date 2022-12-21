.PHONY: all clean test run
all: build test

build: .bin-stamp
	go build -o bin/litserver

run:
	go run ./...

# directories do werid things in make, so we can use a stamp
.bin-stamp:
	mkdir -p bin
	touch .bin-stamp

clean:
	rm -rf bin
	rm .bin-stamp
