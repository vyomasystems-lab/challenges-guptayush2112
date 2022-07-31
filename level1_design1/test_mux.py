# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

"""Test for MUX when Select Line = 1100 [12]"""
@cocotb.test()
async def test_mux(dut):

    """cocotb.log.info('##### CTB: Develop your test here ########')"""
    
    ip12 = 2
    # input driving
    SEL             = 12
    dut.inp0.value  = 0
    dut.inp1.value  = 0
    dut.inp2.value  = 0
    dut.inp3.value  = 0
    dut.inp4.value  = 0
    dut.inp5.value  = 0
    dut.inp6.value  = 0
    dut.inp7.value  = 0
    dut.inp8.value  = 0
    dut.inp9.value  = 0
    dut.inp10.value = 0
    dut.inp11.value = 0
    dut.inp12.value = ip12
    dut.inp13.value = 0
    dut.inp14.value = 0
    dut.inp15.value = 0
    dut.inp16.value = 0
    dut.inp17.value = 0
    dut.inp18.value = 0
    dut.inp19.value = 0
    dut.inp20.value = 0
    dut.inp21.value = 0
    dut.inp22.value = 0
    dut.inp23.value = 0
    dut.inp24.value = 0
    dut.inp25.value = 0
    dut.inp26.value = 0
    dut.inp27.value = 0
    dut.inp28.value = 0
    dut.inp29.value = 0
    dut.inp30.value = 0

    print('\n     Line 40: Bug Found,    Incorrect sel value for input port [inp12]')
    print("     Found: 5'b01101, Expected: 5'b01100\n")

    dut.sel.value = SEL   
    await Timer(2, units='ns')

    assert dut.out.value == ip12, "Mux result is incorrect: When [sel] = {SEL}, [out] != 0, Expected value = {ip12}".format(
            SEL      = int(dut.sel.value), 
            ip12     = int(dut.inp12.value), 
            OUT      = int(dut.out.value))

"""Test for MUX when Select Line = 11110 [30]"""
@cocotb.test()
async def test_mux1(dut):

    ip30 = 1
    # input driving
    SEL             = 30
    dut.inp0.value  = 0
    dut.inp1.value  = 0
    dut.inp2.value  = 0
    dut.inp3.value  = 0
    dut.inp4.value  = 0
    dut.inp5.value  = 0
    dut.inp6.value  = 0
    dut.inp7.value  = 0
    dut.inp8.value  = 0
    dut.inp9.value  = 0
    dut.inp10.value = 0
    dut.inp11.value = 0
    dut.inp12.value = 2
    dut.inp13.value = 0
    dut.inp14.value = 0
    dut.inp15.value = 0
    dut.inp16.value = 0
    dut.inp17.value = 0
    dut.inp18.value = 0
    dut.inp19.value = 0
    dut.inp20.value = 0
    dut.inp21.value = 0
    dut.inp22.value = 0
    dut.inp23.value = 0
    dut.inp24.value = 0
    dut.inp25.value = 0
    dut.inp26.value = 0
    dut.inp27.value = 0
    dut.inp28.value = 0
    dut.inp29.value = 0
    dut.inp30.value = ip30


    dut.sel.value = SEL   
    await Timer(2, units='ns')
    print('\n     Line 58: Bug Found,    Missing sel value for input port [inp30]\n')

    assert dut.out.value == ip30, "Mux result is incorrect: When [sel] = {SEL}, out != 0, Expected value = {ip30}".format(
            SEL      = int(dut.sel.value), 
            ip30     = int(dut.inp30.value), 
            OUT      = int(dut.out.value))