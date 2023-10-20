TARGET:=python-numpy
VERSION:=1.26.1
ARCH:=$(shell uname -m)
OUTPUT:=$(TARGET)-$(VERSION)-1.$(ARCH).rpm
build: $(OUTPUT)

$(OUTPUT): Dockerfile
	docker build --rm -t localhost/pypirpm .
	ID=$$(docker create localhost/pypirpm) \
	&& docker cp $$ID:/rpmbuild/RPMS/$(ARCH)/$(OUTPUT) $(OUTPUT) \
	&& docker rm $$ID
