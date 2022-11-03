
TOPLEVEL_LANG ?= verilog
SIM ?= questa

ifeq ($(TOPLEVEL_LANG),verilog)
  VERILOG_SOURCES = $(shell pwd)/counter.sv
else ifeq ($(TOPLEVEL_LANG),vhdl)
  VHDL_SOURCES = $(shell pwd)/counter.vhdl
endif

MODULE = test_counter
TOPLEVEL = counter

include $(shell cocotb-config --makefiles)/Makefile.sim
