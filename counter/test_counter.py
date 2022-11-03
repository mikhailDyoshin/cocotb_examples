
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge


@cocotb.test()
async def counter_test(dut):
    """Test that counter counts and reset resets"""

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())  # Start the clock

    dut.reset.value = 1 # Initial reset

    for i in range(3):
        await FallingEdge(dut.clk)
        assert dut.res.value == 0, f"output res was incorrect on the {i} cycle"

    dut.reset.value = 0 # reset OFF

    for i in range(10):
        await FallingEdge(dut.clk)
        assert dut.res.value == i+1, f"output res = {dut.res.value} == {i}"

    dut.reset.value = 1 # reset ON

    for i in range(3):
        await FallingEdge(dut.clk)
        assert dut.res.value == 0, f"output res = {dut.res.value} == 0"
    