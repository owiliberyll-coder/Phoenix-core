obj-m += phoenix_core.o

KERNEL_DIR = /lib/modules/$(shell uname -r)/build
PWD := $(shell pwd)

all:
	$(MAKE) -C $(KERNEL_DIR) M=$(PWD) modules

clean:
	$(MAKE) -C $(KERNEL_DIR) M=$(PWD) clean

install:
	sudo insmod phoenix_core.ko

remove:
	sudo rmmod phoenix_core

info:
	modinfo phoenix_core.ko

.PHONY: all clean install remove info
