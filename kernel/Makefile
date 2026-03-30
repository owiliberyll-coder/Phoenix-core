# Makefile for Phoenix Core Kernel Module

KERNEL_BUILD_DIR ?= /lib/modules/$(shell uname -r)/build

MODULE_NAME = phoenix_core
SOURCE = phoenix_core.c

obj-m += $(MODULE_NAME).o

all:
	@echo "Building Phoenix Core kernel module..."
	make -C $(KERNEL_BUILD_DIR) M=$(PWD) modules

clean:
	@echo "Cleaning build artifacts..."
	make -C $(KERNEL_BUILD_DIR) M=$(PWD) clean
	rm -f $(MODULE_NAME).ko $(MODULE_NAME).o $(MODULE_NAME).mod.o $(MODULE_NAME).mod.c Module.symvers modules.order

install:
	@echo "Installing kernel module..."
	sudo make -C $(KERNEL_BUILD_DIR) M=$(PWD) modules_install
	sudo depmod -a

load:
	@echo "Loading kernel module..."
	sudo insmod $(MODULE_NAME).ko

unload:
	@echo "Unloading kernel module..."
	sudo rmmod $(MODULE_NAME) || true

reload: unload load

status:
	@echo "Module status:"
	lsmod | grep phoenix_core || echo "Module not loaded"
	
dmesg:
	@echo "Recent kernel messages:"
	dmesg | tail -20

.PHONY: all clean install load unload reload status dmesg
