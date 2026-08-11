# Appendix G - 6502 Characteristics

## Clocks (Φ1, Φ2)
The MCS 6502 is supplied with an internal clock generator. The frequency of this clock is crystal controlled.

## Address Bus (A0-A15)
These outputs are TIL compatible, capable of driving one standard TTL load and 130pf.

## Data Bus (D0-D7)
Eight pins are used for the data bus. This is a bi-directional bus, transferring data to and from the device and peripherals. The outputs are tri-state buffers capable of driving one standard TTL load and 130pf.

## Ready (RDY)
This input signal allows the user to single cycle the microprocessor on all cycles except write cycles. A negative transition to the low state during or coincident with phase one (Φ1) will halt the microprocessor with the output address lines reflecting the current address being fetched. This condition will remain through a subsequent phase two (Φ2) in which the Ready signal is high. This feature allows microprocessor interfacing with low speed PROMS as well as fast (max. 2 cycle) Direct Memory Access (DMA). If Ready is low during a write cycle, it is Ignored until the following read operation.

## Interrupt Request (<span style="text-decoration: overline;">IRQ</span>)
This TTL level input requests that an interrupt sequence begin within the microprocessor. The microprocessor will complete the current instruction being executed before recognizing the request. At that time, the interrupt mask bit in the Status Code Register will be examined. If the interrupt mask flag is not set, the microprocessor will begin an interrupt sequence. The Program Counter and Processor Status Register are stored in the stack. The microprocessor will then set the interrupt mask flag high so that no further interrupts may occur. At the end of this cycle, the program counter low will be loaded from address FFFE, and program counter high from location FFFF, therefore transferring program control to the memory vector located at these addresses. The RDY signal must be in the high state (for control to the memory vector) located at these addresses. The RDY signal must be in the high state for any interrupt to be recognized. A 3KΩ external register should be used for proper wire-OR operation.

## Non-Maskable Interrupt (<span style="text-decoration: overline;">NMI</span>)
A negative going edge on this input requests that a non-maskable interrupt sequence be generated within the microprocessor. 

<span style="text-decoration: overline;">NMI</span> is an unconditional interrupt. Following completion of the current instruction, the sequence of operations defined for IRQ will be performed, regardless of the state of the interrupt mask flag. The vector address loaded into the program counter, low and high, are locations FFFA and FFFB respectively. The instructions loaded at these locations causes the microprocessor to branch to a non-maskable interrupt routine in memory.

<span style="text-decoration: overline;">NMI</span> also requires an external 3KΩ resistor to Vcc for proper wire-OR operations.

Inputs <span style="text-decoration: overline;">IRQ</span> and <span style="text-decoration: overline;">NMI</span> are hardware interrupts lines that are sampled during Φ2 (phase 2) and will begin the appropriate interrupt routine on the Φ1 (phase 1) following the completion of the current instruction.

## Set Overflow Flag (S.O.)
This TTL level input signal allows external control of the overflow bit in the Status Code Register,

## SYNC
This output line is provided to identify those cycles in which the microprocessor is doing an Op Code fetch. The SYNC line goes high during Φ1 of an Op Code fetch and stays high for the remainder of that cycle. If the RDY line is pulled low during the Φ1 clock pulse in which SYNC went high, the processor will stop in its current state and will remain in the state until the RDY line goes high. In this manner, the SYNC signal can be used to control RDY to cause single Instruction execution.

## RESET (<span style="text-decoration: overline;">RST</span>)
This Input is used to reset or start the microprocessor from a power down condition. During the time that this line is held low, writing to or from the microprocessor is inhibited. When a positive edge is detected on the input, the microprocessor will immediately begin the reset sequence. 

After a system initialization time of six clock, cycles, the mask interrupt flag will be set and the microprocessor will load the program counter from the memory vector locations <code class="HEX">0xFFFC</code> and <code class="HEX">0xFFFD</code>. This is the start location for program control.

After Vcc reaches 4.75 volts in a power up routine, reset must be held low for at least two clock cycles.

When the reset signal goes high following these two clock cycles, the microprocessor will proceed with the normal reset procedure detailed above.
