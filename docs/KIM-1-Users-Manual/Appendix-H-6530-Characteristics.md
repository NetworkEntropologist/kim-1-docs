# Appendix H - 6530 Characteristics

The MCS 6530 is designed to operate in conjunction with the MCS 650X Microprocessor Family. It is comprised of a mask programmable 1024 x 8 ROM, a 64 X 8 static RAM, two software controlled 8 bit bi-directional data ports allowing direct interfacing between the microprocessor unit and peripheral devices, and a software programmable interval timer with interrupt, capable of timing in various intervals from 1 to 262,144 clock periods.

**TODO: Insert Figure H.1 here**

## RESET (<span style="text-decoration: overline;">RST</span>)
During system initialization a Logic "0" on the RES input will cause a zeroing of all four I/O registers. This in turn will cause all I/O buses to act as inputs thus protecting external components from possible damage and erroneous data while the system is being configured under software control. The Data Bus Buffers are put into an OFF-STATE during Reset. Interrupt capability is disabled with the RES signal. The RES signal must be held low for at least one clock period when reset is required.

## Input Clock
**TODO: Insert maths things here**

## Read/Write
The R/W signal is supplied by the microprocessor array and is used to control the transfer of data to and from the microprocessor array and the MCS 6530. A high on the R/W pin allows the  processor to read (with proper addressing) the data supplied by the MCS 6530. A low on the R/W pin allows a write (with proper addressing) to the MCS 6530.

## Interrupt Request (<span style="text-decoration: overline;">IRQ</span>)
The IRQ pin is an interrupt pin from the interval timer. This same pin, if not used as an interrupt, can be used as a peripheral I/O pin (PB7) . When used as an interrupt, the pin should be set up as an input by the data direction register. The pin will be normally high with a low indicating an interrupt from the MCS 6530.

## Data Bus (D0-D7)
The MCS 6530 has eight bi-directional data pins (D0-D7). These pins connect to the system's data lines to allow transfer of data to and from the microprocessor array. The output buffers remain in the off state except when a Read operation occurs.

## Peripheral Data Ports
The MCS 6530-002, MCS 6530-003 both have 15 pins available for peripheral I/O operations. Each pin is individually software programmable to act as either an input or an output. The 15 pins are divided into 2 8-bit ports, PA0-PA7 and PB0-PB7. PB6 was used as a chip select and is not available to the user. The pins are set up as an input by writing a *0* into the corresponding bit of the data direction register. A *1* into the data direction register will cause its corresponding bit to be an output. When in the input mode, the peripheral output buffers are in  the *1* state and a pull-up device acts as less than one TTL load to the peripheral data lines. On a Read operation, the microprocessor unit reads the peripheral pin. When the peripheral device gets information from the MCS 6530 it receives data stored in the data register. The microprocessor will read correct information if the peripheral lines are greater than 2.0 volts for a *1* and less than 0.8 volts for a *0* as the peripheral pins are all TTL compatible. Pins PA0 and PB0 are also capable of sourcing 3 ma at 1.5v, thus making them capable of Darlington drive. Pin PB7 has no internal pull-up (to allow collector-oring with other devices).

## Address Lines (A0-A9 )
There are 10 address pins. In addition to these 10, there is the ROM SELECT pin. The above pins, A0-A9 and ROM SELECT, are always used as addressing pins. There are 2 additional pins which are mask programmable and can be used either individually or together as CHIP SELECTS. They are pins PB5 and PB6. When used as peripheral data pins they cannot be used as chip selects. PB5 was used as a data pin while PB6 was used as a chip select and is not available to the user.

A block diagram of the internal architecture is shown in Figure H-1. The MCS 6530 is divided into four basic sections, MM, ROM, I/O and TIMER. The RAM and ROM interface directly with the microprocessor through the system data bus and address lines. The I/O section consists of 2 8-bit halves. Each half contains a Data Direction Register (DDR) and an I/O Register.

## ROM IK Byte (8K Bits)
The 8K ROM is in a 1024 x 8 configuration. Address lines A0-A9, as well as RSO are needed to address the entire ROM. With the addition of CSl and CS2 , seven MCS 6530's may be addressed,  giving 7168 X 8 bits of contiguous ROM.

## RAM 64 Bytes (512 Bits)
A 64 X 8 static RAM is contained on the MCS 6530. It is addressed by A0-A5 (Byte Select), RS0, A6, A7 , A8, A9 and CS1.

## Internal Peripheral Registers
There are four internal registers, two data direction registers and two peripheral I/O data registers. The two data direction registers (A side and B side) control the direction of the data into and out of the peripheral pins. A "1" written into the Data Direction Register sets up the corresponding peripheral buffer pin as an output. Therefore, anything then written into the I/O Register will appear on that corresponding peripheral pin. A "0" written into the DDR inhibits the output buffer from transmitting data to or from  the I/O Register. For example, a "1" loaded into data direction register A, position 3, sets up peripheral pin PA3 as an output. If a "0" had been loaded, PA3 would be configured as an input and remain in the high state. The two data I/O registers are used to latch data from the Data Bus during a Write operation until the peripheral device can read the data supplied by the microprocessor array.

During a read operation the microprocessor is not reading the I/O Registers but in fact is reading the peripheral data pins. For the peripheral data pins which are programmed as outputs the microprocessor will read the corresponding data bits of the I/O Register. The only way the I/O Register data can be changed Is by a microprocessor Write operation. The I/O Register is not affected by a read of the data on the peripheral pins.

## Interval Timer

### Capabilities
The KIM-1 Interval Timer allows the user to specify a preset count of up to 256 and a clock divide rate of 1, 8, 64 or 1024 by writing to a memory location. As soon as the write occurs, counting at the specified rate begins. The timer counts down at the clock frequency divided by the divide rate. The current timer count may be read at any time. At the user's option, the timer may be programmed to generate an interrupt when the counter counts down past zero. When a count of zero is passed, the divide rate is automatically set to 1 and the counter continues to count down at the clock rate starting at a count of <code class="HEX">0xFF</code> (-1 in two's complement arithmetic). This allows the user to determine how many clock cycles have passed since the timer reached a count of zero. Since the counter never stops, continued counting down will reach 00 again, then FF, and the count will continue.

### Operation

#### Loading the timer
The divide rate and interrupt option enable/disable are programmed by decoding the least significant address bits. The starting count for the timer is determined by the value written to that address.

| Writing to Address | Sets Divide Ratio To | Interrupt Capability Is |
|:---:|----:|:---:|
| <code class="HEX">0x1704</code> | 1 | Disabled |
| <code class="HEX">0x1705</code> | 8 | Disabled |
| <code class="HEX">0x1706</code> | 64 | Disabled |
| <code class="HEX">0x1707</code> | 1024 | Disabled |
| <code class="HEX">0x170C</code> | 1 | Disabled |
| <code class="HEX">0x170D</code> | 8 | Disabled |
| <code class="HEX">0x170E</code> | 64 | Disabled |
| <code class="HEX">0x170F</code> | 1024 | Disabled |

#### Determining the timer status
After timing has begun, reading address location <code class="HEX">0x1707</code> will provide the timer status. If the counter has passed the count of zero, bit 7 will be set to 1, otherwise, bit 7 (and all other bits in location <code class="HEX">0x1707</code>) will be zero. This allows a program to "watch" location 1707 and determine when the timer has timed out.

#### Reading the count in the timer
If the timer has not counted past zero, reading location <code class="HEX">0x1706</code> will provide the current timer count and disable the interrupt option; reading location <code class="HEX">0x170E</code> will provide the current timer count and enable the interrupt option. Thus the interrupt option can be changed while the timer is counting down.

If the timer has counted past zero, reading either memory location <code class="HEX">0x1706</code> or <code class="HEX">0x170E</code> will restore the divide ratio to its previously programmed value, disable the interrupt option and leave the timer with its current count (not the count originally written to the timer). Because the timer never stops counting, the timer will continue to decrement, pass zero, set the divide rate to 1, and continue to count down at the clock frequency, unless new information is written to the timer.

#### Using the interrupt option
In order to use the interrupt option described above, line PB7 (application connector, pin 15) should be connected to either the <span style="text-decoration: overline;">IRQ</span> (Expansion Connector, pin 4) or <span style="text-decoration: overline;">NMI</span> (Expansion connector, pin 6) pin depending on the desired interrupt function. PB7 should be programmed as in input line (it's normal state after a RESET).

**NOTE:** If the programmer desires to use PB7 as a normal I/O line, the programmer is responsible for disabling the timer interrupt option (by writing or reading address <code class="HEX">0x1706</code>) so that it does not interfere with normal operation of PB7. Also, PB7 was designed to be wire-ORed with other possible interrupt sources; if this is not desired, a 5.1K resistor should be used as a pull-up from PB7 to +5v. (The pull-up should NOT be used if PB7 is connected to <span style="text-decoration: overline;">NMI</span> or <span style="text-decoration: overline;">IRQ</span>.)