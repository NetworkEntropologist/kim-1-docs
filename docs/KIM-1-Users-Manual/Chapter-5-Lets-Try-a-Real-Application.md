**TODO: Add links to appendixes**

# Chapter 5 - Let's Try a Real Application

It is not practical in this manual to describe every possible application or progrannning technique. However, now that you have become familiar with the basic elements and operating procedures of the KIM-1 system, this section will show you how to apply what you have learned in a simple but realistic application example.

Our example will involve the generation of a variable frequency square wave which will be connected to a speaker to produce an audible tone. The frequency of the tone will be selected using a set of seven toggle switches. We will proceed through the example by defining the interface, writing and entering the program, and executing the program. Finally, we will study a series of program debugging techniques which will be useful to you for any new program you may write.

## Defining the Interface
You will recall that a group of 15 I/O pins are brought to the Application connector from the 6530-003 array. The logic and circuit details concerning these I/O pins are described in Appendix H and in Section 1.6 of the Hardware Manual (*Peripheral Interface/Memory Device MCS 6530*).

For our application example we will use eight of these I/O pins. One pin (PA0) will be used as an output line to supply a square wave to a driver circuit and speaker. The other seven I/O pins (PAl to PA7) are defined as input points with a SPST toggle switch connected to each. Figure 5-1 shows the circuit configuration for this example. Note that the remaining seven I/O pins (the PB port) are not used for this problem.

For the switches connected to the input pins, we would like the sense of the switch to be defined as a logic "0" when open and a logic "1" when closed. By connecting the switches to ground, we are producing exactly the opposite sense and must remember to complement the switch states with software when we write our program. Also, we must define now that the switch at PAl is to be the LSB (least significant bit) and the switch at PA7 is to be the MSB (most significant bit) of the seven bit binary word formed by all seven switches. In this way, the state of the switches can define a binary number from zero (all switches open) to 127<sub>DEC</sub> (all switches closed).

**TODO: Insert figure 5.1 here**

## Writing the Program
Having defined the interface for our application, we may proceed now to write our program. The effort proceeds in four stages:

1. Generate a flow chart
2. Generate assembly language code
3. Analyze the program
4. Generate machine language code

**TODO: Insert flowchart from page 58 here**

Briefly, our flow chart shows a first step of system initialization. During this step, we must define the I/O configuration of the system in that pin PA0 becomes the output to the speaker and that pins PAl to PA7 become inputs from the seven switches.

After initialization, a loop is set up which begins by inverting the state of PACi (Toggle PA0) . Next, the state of the switches is read and the data is complemented to produce the correct "sense" from the switches. The value so read is used to define a delay before returning to the start of the loop and again toggling the state of PA0. A little thought will
show that this loop will produce a square wave with a frequency determined by the setting of the seven switches.

### Assembly Language Program
Our next task is to convert the simple flow chart into a program. The program is first written in "Assembly Language". You should refer to your Programming Manual to become familiar with all of the possible 6502 instructions (especially see Appendix B; Instruction Summary). Figure 5-2 shows the application example programmed in assembly language.

**TODO: Insert ASM listing from page 60 here**

You will note that each line of the program is broken into several fields:

- A label field permitting you to assign a "name" to a specific location in the program.<br>
- An Operation Code field (Op Code) in which the exact instruction to be executed is defined.<br>
- An Operand Field where the exact data required by the instruction is defined together with certain symbols defining addressing modes or data formats. Symbols encountered generally in MOS Technology, Inc. manuals are:

| SYMBOL | MEANING |
|:------:|---------|
| # | Immediate Addressing |
| $ | Hex Code |
| @ | Octal Code |
| % | Binary Code |
| t |  ASCII literal |
| = | Equates a label to a value |

- A Machine Cycle field defining the total number of machine cycles required to execute an instruction. (This information is derived from Appendix B of the Programming Manual).<br>
- A Comment Field where the programmer may define the intent of specific program steps.<br>

### Program Analysis
The inclusion of the "machine cycle" information of the program chart (Figure 5-2) allows us to analyze the exact timing relationships involved in our program example. Note that the KIM-1 system operates from a fixed frequency (1 MHz) oscillator with each machine cycle being lys. Therefore, an instruction like "INC PAD" which requires 6 machine cycles will be executed in a 6µs period.

By counting the total machine cycles occurring between each toggle of PA0 an equation for the square wave frequency can be developed. The actual frequency is determined by the position of the seven switches, the number of machine cycles between each toggle of PA0, and the basic clock rate (1 MHz) of the KIM-1 system. Figure 5-3 shows the waveform of the PA0 square wave and the derived equations for computing the exact frequency.

**TODO: Insert figure 5.3 here**

### Machine Language Coding
Our next problem is to convert our assembly language program into a program written in "machine language". The quickest and most foolproof method for accomplishing this conversion is by using the MOS Technology, Inc. Assembler (available for use on the time share services of United Computing Systems, Inc.). If you choose not to use this method, you will need to convert your source program to machine code using "paper-and-pencil" techniques. You should proceed by constructing a table similar to that shown in Figure 5-4.

**TODO: Insert figure 5.4 here**

The source code contained in your assembly language program (Figure 5-2) is entered into the table first. A column is provided to allow you to define the specific address at which an instruction is located. The Instruction column provides space for defining one, two, or three byte instructions. (Please refer to Appendix B of the Programming Manual or to your Programming Card for specific OP Codes).

As an example, the first source instruction is ```LDA #$01``` which, when translated, means load the accumulator with the byte stored in the next program location (hex 01) . This is the "immediate" addressing mode defined by the "#" symbol. The Op Code for ```LDA#``` is ```A9```. This value is entered in the first column under the heading, Instruction. The next column contains the hex 01 value defined by the source statement. The initial address for the program is inserted in the "Address" column as ```0200``` (an arbitrary selection). The total instruction ```LDA #$01``` now occupies address locations ```0x0200``` and ```0x0201```.

The next available address is ```0x0202``` which is inserted in the "Address" column for the next source Instruction. In this manner, you will proceed through all of the source statements decoding each and entering one, two, or three bytes of machine code as required in the "Instruction" column. The "Address" column will contain the address of the first byte of machine code (the Op Code) for each source statement.

In cases where the operand of the source statement is a symbol, the address to which the symbol has been equated should be filled in as the proper machine code. For example, the source statement ```INC PAD``` requires the incrementing of data stored at a location ```PAD``` defined in our assembly programs to have the address: ```PAD = 1700```. Therefore, the address ```1700``` is entered as the second and third bytes of the source statement ```INC PAD```. (See Figure 5-4). Note also that when entering an address, such as ```1700```, the low order byte (00) is entered first and immediately after the OP Code and the high order byte (17) is entered next as the third byte of the instruction.

When dealing with branch instructions (```BPL```, ```BMI```, etc.), you will need to calculate the exact value of the offset which may be either positive (branch forward) or negative (branch backward) . You should refer to Section 4.1.1 of the Programming Manual to explore *Basic Concept of Relative Branching*. As an example, the source statement ```BMI START``` (See
Figures 5-2 and 5-4) requires a branch backward by (-15) locations to the address labelled *START* (from address ```0x0213``` backward to ```0x0205``` inclusive).

(The 2's complement of the -15 displacement is ```0xFl``` which you should insert at location ```0x0212```). Had the branch been to a forward location the positive value of the offset would be inserted rather than the 2's complement value.

## Entering the Program
With the program now reduced to machine language code, you may enter the program address and data codes listed below following the procedures detailed in the section [Let's try a simple program](Chapter-2-Getting-Started.md#lets-try-a-simple-program) in [Chapter 2](Chapter-2-Getting-Started.md). The procedure for entering the program is as follows:

| Press Keys | See On Display |
|---|:---:|
| <kbd>AD</kbd> <kbd>0</kbd> <kbd>2</kbd> <kbd>0</kbd> <kbd>0</kbd> | <samp>0200 xx</samp> |
| <kbd>DA</kbd> <kbd>A</kbd> <kbd>9</kbd> | <samp>0200 A9</samp> |
| <kbd>+</kbd> <kbd>0</kbd> <kbd>1</kbd> | <samp>0201 01</samp> |
| <kbd>+</kbd> <kbd>8</kbd> <kbd>D</kbd> | <samp>0202 8D</samp> |
| <kbd>+</kbd> <kbd>0</kbd> <kbd>1</kbd> | <samp>0203 01</samp> |
| <kbd>+</kbd> <kbd>1</kbd> <kbd>7</kbd> | <samp>0204 17</samp> |
| <kbd>+</kbd> <kbd>E</kbd> <kbd>E</kbd> | <samp>0205 EE</samp> |
| <kbd>+</kbd> <kbd>0</kbd> <kbd>0</kbd> | <samp>0206 00</samp> |
| <kbd>+</kbd> <kbd>1</kbd> <kbd>7</kbd> | <samp>0207 17</samp> |
| <kbd>+</kbd> <kbd>A</kbd> <kbd>D</kbd> | <samp>0208 AD</samp> |
| <kbd>+</kbd> <kbd>0</kbd> <kbd>0</kbd> | <samp>0209 00</samp> |
| <kbd>+</kbd> <kbd>1</kbd> <kbd>7</kbd> | <samp>020A 17</samp> |
| <kbd>+</kbd> <kbd>4</kbd> <kbd>9</kbd> | <samp>020B 49</samp> |
| <kbd>+</kbd> <kbd>F</kbd> <kbd>F</kbd> | <samp>020C FF</samp> |
| <kbd>+</kbd> <kbd>4</kbd> <kbd>A</kbd> | <samp>020D 4A</samp> |
| <kbd>+</kbd> <kbd>A</kbd> <kbd>A</kbd> | <samp>020E AA</samp> |
| <kbd>+</kbd> <kbd>C</kbd> <kbd>A</kbd> | <samp>020F CA</samp> |
| <kbd>+</kbd> <kbd>1</kbd> <kbd>0</kbd> | <samp>0210 10</samp> |
| <kbd>+</kbd> <kbd>F</kbd> <kbd>D</kbd> | <samp>0211 FD</samp> |
| <kbd>+</kbd> <kbd>3</kbd> <kbd>0</kbd> | <samp>0212 30</samp> |
| <kbd>+</kbd> <kbd>F</kbd> <kbd>1</kbd> | <samp>0213 F1</samp> |

## Executing the Program
With the program entered, you may proceed to program execution. First, if the NMI vector has not been defined previously, enter the vector as follows:

| Press Keys | See Displayed |
|---|:---:|
| <kbd>AD</kbd> <kbd>1</kbd> <kbd>7</kbd> <kbd>F</kbd> <kbd>A</kbd> | <samp>17FA xx</samp> |
| <kbd>DA</kbd> <kbd>0</kbd> <kbd>0</kbd> | <samp>17FA 00</samp> |
| <kbd>+</kbd> <kbd>1</kbd> <kbd>C</kbd> | <samp>17FB 1C</samp> |

This procedure insures that the <kbd>ST</kbd> key will be effective in terminating the program. Now, select the starting address of your
program (```0x0200```) and begin execution as follows:

| Press Keys | See Displayed |
|---|:---:|
| <kbd>AD</kbd> <kbd>0</kbd> <kbd>2</kbd> <kbd>0</kbd> <kbd>0</kbd> | <samp>0200 A9</samp> |
| <kbd>GO</kbd> | (Dark) |

The program will now execute. If your seven selector switches all are open, you will probably hear no sound from the speaker because the square wave frequency is too high. If all selector switches are closed, you will hear in the speaker the lowest frequency that can be generated with the program as currently written. You may experiment with other combinations of switch settings to hear a variety of tones from the speaker.

Depression of the <kbd>ST</kbd> key will cause the program execution to stop (the tone will terminate) and the KIM-1 display will relight. The display will show the address and data for the next instruction to be executed (probably ```0x020F``` or ```0x0210``` since this is the delay loop where the program spends most of its running time).

## Program Debugging and Modification
If your program did not execute correctly, you would follow a debugging procedure involving the following steps:

**Step 1: List the Program:** First make sure you have entered the program steps correctly. Select the starting address ( <kbd>AD</kbd><kbd>0</kbd><kbd>2</kbd><kbd>0</kbd><kbd>0</kbd>) and observe that the correct data (A9) is displayed. Now, using the <kbd>+</kbd> key, step through the remaining program locations checking for the correct data stored in each location.

**Step 2: Single Step the Program:** Follow the procedures listed in Section 5-4 for program execution but before depressing the go key, place the SST slide switch in the ON position. Now, press the go key and the first instruction will be executed. The display will relight indicating that the operating program is again in control of the system. The address displayed will be the address of the first byte of the next instruction to be executed. You may press the go key again to execute the next instruction or you may choose to investigate changes in the contents of machine registers stored in selected memory locations (See Figure 3-13). The procedure detailed in Figure 5-6 gives a good indication of the various operations you may wish to perform in the SST mode.

**Step 3: Check the I/O Operations:** If program entry has been verified and program execution in the SST mode appears to be normal, you may wish to verify the correct operation of your specific I/O configuration. 

You should recall that writing to or reading from any I/O port is the same as reading from or writing to any other memory location in the system. Therefore, if you select the address of an I/O port, the KIM-1 display will show you the hex code for the data being read from that address and thus, directly indicate the state of each I/O pin in the port. For example, the address of the I/O port used for your sample program is ```0x1700```. Press <kbd>AD</kbd><kbd>1</kbd><kbd>7</kbd><kbd>0</kbd><kbd>0</kbd> and the display will show the hex code corresponding to the settings of your selector switches. If you change the positions of your selector switches, you will sec the hex code ch^ge In the data field of the display.

Now, leave the same address (```0x1700```) selected and press the <kbd>DA</kbd> key. If you press any of the hex keys <kbd>0</kbd> to <kbd>F</kbd>, you will write the data to the I/O port (```0x1700```). Since seven of the pins of this I/O port are defined as inputs, only one (PA0) will act as an output and will respond to the data entered by you from the keyboard. Try alternating rapidly between the <kbd>0</kbd> to <kbd>1</kbd> keys and you should hear clicking in the speaker indicating that you are successfully toggling the PA0 pin.

This concept of using the KIM-1 keyboard and display to exercise and verify the operation of I/O ports is a generally useful technique for debugging the hardware portions of most specific applications.

| Press Keys | See Displayed | Comments |
|---|:---:|---|
| <kbd>AD</kbd> <kbd>0</kbd> <kbd>2</kbd> <kbd>0</kbd> <kbd>0</kbd> | <samp>0200 A9</samp> | Select first instruction address |
| <span class="switch" data-pos="ON">SST</span> | <samp>0200 A9</samp> | Set SST to ON; All selector switches open |
| <kbd>GO</kbd> | <samp>0202 8D</samp> | Accumulator now loaded with <code class="hex">$01</code> |
| <kbd>GO</kbd> | <samp>0205 EE</samp> | PADD now loaded |
| <kbd>GO</kbd> | <samp>0208 AD</samp> | PA0 now toggled |
| <kbd>GO</kbd> | <samp>020B 49</samp> | Switch values (PA1-PA7) now loaded |
| <kbd>GO</kbd> | <samp>020D 4A</samp> | Accumulator now complemented |
| <kbd>GO</kbd> | <samp>020E AA</samp> | Accumulator now right shifted 1 Bit |
| <kbd>AD</kbd> <kbd>0</kbd> <kbd>0</kbd> <kbd>F</kbd> <kbd>3</kbd> | <samp>00F3 xx</samp> | Display Accumulator |
| <kbd>+</kbd> | <samp>00F4 xx</samp> | Display Y - INDEX |
| <kbd>+</kbd> | <samp>00F5 00</samp> | Display X - INDEX |
| <kbd>PC</kbd> | <samp>020E AA</samp> | Restore PC (`TAX` will execute next) |
| <kbd>GO</kbd> | <samp>020F CA</samp> | Accumulator now loaded in X-INDEX |
| <kbd>AD</kbd> <kbd>0</kbd> <kbd>0</kbd> <kbd>F</kbd> <kbd>3</kbd> | <samp>00F3 00</samp> | Display Accumulator |
| <kbd>+</kbd> | <samp>00F4 xx</samp> | Display Y-INDEX |
| <kbd>+</kbd> | <samp>00F5 00</samp> | Display X-INDEX (A=0→X) |
| <kbd>PC</kbd> | <samp>020F CA</samp> | Restore PC |
| <kbd>GO</kbd> | <samp>0210 10</samp> | `DEX` now completed |
| <kbd>AD</kbd> <kbd>0</kbd> <kbd>0</kbd> <kbd>F</kbd> <kbd>5</kbd> | <samp>00F5 FF</samp> | Display X-INDEX (X<0) |
| <kbd>PC</kbd> | <samp>0210 10</samp> | Restore PC |
| <kbd>GO</kbd> | <samp>0212 30</samp> | No branch (Result of `DEX` *not* positive) |
| <kbd>GO</kbd> | <samp>0205 EE</samp> | Branch (Result of `DEX` *is* negative). |
