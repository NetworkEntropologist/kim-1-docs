**TODO: Add references to Appendixes**

# Chapter 4 - Operating the KIM-1 System

Now that you have a better idea of what is included in your KIM-1 system and haw it operates, its time to provide you with detailed procedures for all of the operations you can perform with the system. We will separate our operating procedures into three areas giving specific direction for the use of the KIM-1 keyboard and display, the audio tape recorder, and the serial teleprinter (TTY).

## Using the KIM-1 Keyboard and Display
A brief study of your keyboard shows a total of 23 keys and one slide switch. First, let's list the purpose of each key:

<kbd>0</kbd> TO <kbd>F</kbd> - Sixteen keys used to define the hex code of address or data

<kbd>AD</kbd> - selects the address entry mode selects

<kbd>DA</kbd> - selects the data entry mode 

<kbd>+</kbd> - increments the address by +1 but does not change the entry mode

<kbd>PC</kbd> - recalls the address stored in the Program Counter locations (PCH, PCL) to the display

<kbd>RS</kbd> - causes a total system reset and a return to the control of the operating program

<kbd>GO</kbd> - causes program execution to begin starting at the address shown on the display

<kbd>ST</kbd> - terminates the execution of a program and causes a return to the control of the operating program

You have seen in an earlier chapter that the six digit display includes a four digit display of an address (left four digits) and a two digit display of data (right two digits).

Using only the KIM-1 keyboard and display, you may perform any of the following operations:

**1. Select an Address**
Press AD followed by any four of the hex entry keys. The address selected will appear on the display. If an entry error is made, just continue to enter the correct hex keys until the desired address shows on the display. Regardless of what address is selected, the data field of the display will show the data stored at that address.

**2. Modify Data**
After selecting the proper address, press <kbd>DA</kbd> followed by two hex entry keys which correctly define the data to be stored at the selected address. The data entered will appear in the data field of the display to indicate that the desired code has already been entered. Note that it is possible for you to-select an address of a ROM memory cell or even the address of a memory cell that does not exist in your system. In these cases, you will not be able to change the data display since it is clearly not possible for the system to write data to a ROM cell or a non-existent memory location.

**3. Increment the Address**
By pressing the <kbd>+</kbd> key the address displayed is automatically increased by +1. Of course, the data stored at the new address will appear on the display. This operation is useful when a number of successive address locat ions must be read or modified. Note that the use of the <kbd>+</kbd> key will
not change the entry mode. If you had previously pressed the AD key, you remain in the address entry mode and a previous depression of the <kbd>DA</kbd> means you remain in the data entry mode.

**4. Recall Program Counter**
Whenever the NMI Interrupt pin of the 6502 microprocessor array is activated, the program execution in progress will halt and the internal  registers of the 6502 are saved in special memory locations before the control of the system is returned to the operating program. In the KIM-1 system, the NMI interrupt may occur in response to a depression of the <kbd>ST</kbd> key (stop) or, when operating in the Single Step mode, after each program instruction is executed following the depression of the GO key. The <kbd>PC</kbd> key allows you automatically to recall the value of the Program Counter at the time an interrupt occurred. You may have performed a variety of operations since the interrupt such as inspecting the contents of various machine registers stored at specific memory locations. However, when you press the <kbd>PC</kbd> key, the contents of the Program Counter at the time ot the interrupt are recalled to the address field of the display. You now may continue program execution from that point by pressing the go key.

**5. Execute a Program**
Select the starting address of the desired program. Now, press the <kbd>GO</kbd> key and program execution will commence starting with the address appearing on the display.

**6. Terminate a Program**
The <kbd>ST</kbd> key is provided to allow termination of program execution . As mentioned earlier, the <kbd>ST</kbd> key activates the NMI interrupt input of the 6502 microprocessor array.

Note: The <kbd>ST</kbd> key will operate correctly only if you store the correct interrupt vector at locations 17FA and 17FB. For most of your work with the KIM-1 system, you should store the address ICOO in these locations as follows:

Now, when the <span style="text-decoration: overline;">NMI</span> interrupt occurs, the program will return to location ICOO and will proceed to save all machine registers before returning control to the operating program. 

You should remember to define the <span style="text-decoration: overline;">NMI</span> vector each time the power to the system has been interrupted. A failure of the system to react to the <kbd>ST</kbd> key means you have forgotten to define the <span style="text-decoration: overline;">NMI</span> vector.

**7. Single Step Program Execution**
In the process of debugging a new program, you will find the single step execution mode helpful. To operate in this mode, move the SST slide switch to the ON position (to your right). Now, depress the go key for each desired execution of a program step. The display will show the address and data for the next instruction to be executed. Note that in the course of stepping through a program, certain addresses will appear to be skipped. A program instruction will occupy one, two, or three bytes of memory depending upon the type of instruction. In single instruction mode, all of the bytes involved in the execution of the Instruction are accessed and the program will halt only on the first byte of each successive instruction.

*Note:* SST mode also makes use of the NMI interrupt of the 6502 microprocessor array. Again, the NMI vector must be defined as described in (6) above if the SST mode is to work correctly.

This covers all of the standard operations you may perform from the KIM-1 keyboard. Using combinations of the operations described, you may wish to perform certain specialized tasks as follows:

**1. Define the IRQ Vector**
You will recall that a separate interrupt input labelled <span style="text-decoration: overline;">IRQ</span> is available as an input to the 6502 microprocessor array. If you wish to use this feature, you should enter the address to which the program will jump. The <span style="text-decoration: overline;">IRQ</span> vector is stored in locations 17FE and 17FF.

**2. Interrogate Machine Status**
We have mentioned that after an NMI interrupt in response to the <kbd>ST</kbd> key or during the SST mode, the contents of various machine registers are stored in specific memory locations. If you wish to inspect these locations, their addresses are:

| ADDRESS | FUNCTION |
|:-------:|----------|
| OOEF | PCL |
| OOFO | PCH |
| OOF1 | Status Register (P) |
| 00F2 | Stack Pointer (SP) |
| 00F3 | Accumulator (A) |
| 00F4 | Y Index Register |
| 00F5 | X Index Register |

## Using the Audio Tape Recorder
There are two basic operations possible when working with your audio tape system. You may transfer data from the KIM-1 memory and record it on  tape. Or, you may read back a previously recorded tape, transferring the data on tape into the KIM-1 memory.

### Recording on Audio Tape
The procedure for recording on audio tape requires that you perform the following steps:

1. Clear decimal mode by entering 00 in location OOFl. Define an Identification number (ID) for the data block you are about to record. This two digit number is loaded into address 17F9. Don't use ID = 00 or ID = FF.

2. Define the starting address of the data block to be transferred. This address is to be loaded into locations:

| ADDRESS | FUNCTION |
|:-------:|----------|
| 17F5 | Starting Address Low (SAL) |
| 17F6 | Starting Address High (SAH) |

3. Define the ending address as one greater than the last address in the data block to be recorded. The ending address is to be loaded into locations:

| ADDRESS | FUNCTION |
|:-------:|----------|
| 17F7 | End Address Low (EAL) |
| 17F8 | End Address High (EAH) |

As an example, assume you wish to record a data block from address 0200 up to and including address 03FF. (All of Pages 2 and 3). You wish to assign an ID number of 05 to this block. Using the KIM-1 keyboard, you should load the data shown into the addresses indicated so that:

| ADDRESS | FUNCTION |
|:-------:|----------|
| OOFl | 00 (Clear Decimal Mode) |
| 17F5 | 00 (SAL) |
| 17F6 | 02 (SAH) |
| 17F7 | 00 (EAL)* |
| 17F8 | 04 (EAH)* |
| 17F9 | 06 (ID) |
\* 03FF + 1

Note that the ending address must be greater than the starting address for proper operation.

4. Assuming that you are using a new cassette on which no data has been stored previously, insert the cassette in the unit and rewind the tape to its start position.<br>
5. Select the starting address of the tape record program. This address is 1800.<br>
6. Select the Play/Record mode of the audio unit and allow several seconds for the tape to begin to move.<br>
7. Press the <kbd>GO</kbd> key and the recording process will begin. The display will be blanked for a period and then will relight showing `0000 xx`. This means that the data block selected has been recorded.<br>
8. You may now stop the tape or allow some additional seconds of blank tape and then stop the unit.

### Loading Data From Audio Tape
The procedure for loading data from an audio tape into the KIM-1 memory requires that you perform the following steps:

1. Clear decimal mode by entering 00 in location OOFl. Define the ID number of the data block to be loaded from tape. The ID number is loaded into address 17F9.<br>
2. Select the starting address of the Tape Load program. This address is <code class="hex">0x1873</code>.<br>
3. Press the <kbd>GO</kbd> key. The KIM-1 system is now waiting for the appearance of data from the tape unit.<br>
4. Load the cassette and, presuming you do not know where on the tape the data block is recorded, rewind the tape to its starting position. Check the volume control setting.<br>
5. Start the audio tape unit in its Play mode and observe that the tape begins to move.<br>
6. Wait for the KIM-1 display to relight showing <samp>0000 xx</samp>. This means the data block has been loaded successfully from the tape into the KIM-1 memory. If the display relights with <samp>FFFF xx</samp>, the correct data block has been found but there has been an error detected during the read operation. If the tape continues to run and the display never relights, the system has not been successful in finding the data block with the specific ID number you requested.<br>
7. If in step (1), you had selected an ID = 00, the ID number recorded on the tape will be ignored and the system will read the first valid data block encountered on the tape. The data read from the tape will be loaded into memory address as specified on the tape.<br>
8. If, in step (1), you had selected an ID = FF, the ID number recorded on the tape will be ignored and the system will read the first valid data block encountered on the tape. In addition, the data block will be loaded into successive memory locations beginning at the address specified in locations 17F5 and 17F6 (SAL, SAH) instead of the locations specified on the tape.

### Special Operations with Audio Tape
The KIM-1 system causes data to be recorded on audio tape with a specific format as detailed in Appendix E. Each recorded data block is preceeded by a group of synchronizing characters together with an identification code to define the specific block. Data blocks may be of arbitrary length.

With a little care, there is no reason for you not to include a number of recorded data blocks on the same tape. If you are recording blocks in sequence and have not rewound the tape between blocks, you need only specify the parameters of each new block (ID, SAL, SAH, EAH, EAL) and proceed with recording the new block.

If the tape has been rewound, you will need to know the ID number of the last recorded data block. Rewind the tape to its starting point and set up the parameters required to read the last recorded data block. After reading this block, stop the tape and you may now proceed to add a new block or blocks to the tape.

If you wish, you may add voice messages between the recorded data blocks on the tape. The KIM-1 system will ignore these audio messages when the tape is read back. Of course, you will need to install an earphone or speaker in parallel with the KIM-1 audio tape data input pin in order to hear the voice messages.

We **do not** recommend that you attempt to record data blocks in areas of the tape which have been used previously for recorded data. Variations in tape speed and block lengths can result in overlapping of recorded data which may be read incorrectly by the KIM-1 system.

## Using a Serial Teleprinter
The addition of a serial teleprinter (such as the Teletype Model 33ASR) to work with the KIM-1 system permits a variety of special operations to be performed. In all cases , you define desired operations by depressing the proper keys while simultaneously producing a hard-copy printed record of each operation. If your teleprinter is equipped with a paper tape reader/punch, you may generate or read paper tapes using the KIM-1 system. Using the serial teleprinter, you may perform the following operations:

**Select an Address:** Type four hex keys (0 to F) to define the desired address. Next, press <kbd>SPACE</kbd>. The printer will respond showing the address code selected followed by a two digit hex code for data stored at the selected address location:

| Type | Printer Responds |
|------|------------------|
| <kbd>1</kbd><kbd>2</kbd><kbd>3</kbd><kbd>4</kbd> <kbd>SPACE</kbd> | <samp>1234 AF</samp> |

showing that the data AF is stored at location <code class="HEX">0x1234</code>.

**Modify Data:** Select an address as in the previous section. Now type two hex characters to define the data to be stored at that address. Next type the <kbd>.</kbd> key to authorize the modification of data at the selected address:

| Type | Printer Responds |
|------|------------------|
| <kbd>1</kbd><kbd>2</kbd><kbd>3</kbd><kbd>4</kbd> <kbd>SPACE</kbd> | <samp>1234 AF</samp> |
| <kbd>6</kbd><kbd>D</kbd><kbd>.</kbd> | <samp>1235 B7</samp> |

Note that the selected address (<code class="HEX">0x1234</code>) has been modified and the system increments automatically to the next address (<code class="HEX">0x1235</code>).

*Note:* Leading zero's need not be entered for either address or data fields: For example:

EF <kbd>SPACE</kbd> selects address OOEF <br>
E <kbd>SPACE</kbd> selects address OOOE <br>
A <kbd>.</kbd> enters data OA <br>
<kbd>.</kbd> enters data 00 (etc.)

**Step to Next Address:** Type <kbd>CR</kbd> to step to the next address without modifying the current address:

| Type | Printer Responds |
|------|------------------|
| | <samp>1234 AF</samp> |
| <kbd>CR</kbd> | <samp>1235 B7</samp> |
| <kbd>CR</kbd> | <samp>1236 CB</samp> |

**Step to Preceeding Address:** Type <kbd>LF</kbd> to step back to the preceeding address:

| Type | Printer Responds |
|------|------------------|
| | <samp>1234 AF</samp> |
| <kbd>LF</kbd> | <samp>1233 9D</samp> |
| <kbd>LF</kbd> | <samp>1232 8E</samp> |

Abort Current Operation
Type <kbd>RUB OUT</kbd> to terminate the current operation. The prompting message will be printed (<samp>KIM</samp>) indicating that a new operation may proceed:

| Type | Printer Responds |
|------|------------------|
| <kbd>1</kbd><kbd>2</kbd><kbd>6</kbd><kbd>4</kbd><kbd>RUB OUT</kbd> | <samp>KIM<br>XXXX XX</samp> |
| <kbd>6</kbd><kbd>D</kbd><kbd>.</kbd> | <samp>1235 B7</samp> |
| <kbd>1</kbd><kbd>2</kbd><kbd>3</kbd><kbd>4</kbd><kbd>SPACE</kbd> | <samp>1234 AF</samp> |

In the example, the <kbd>RUB OUT</kbd> key is used to correct an erroneous address selection.

*Note:* The <kbd>RUB OUT</kbd> key must be depressed after each depression of the KIM-1 reset key in order to allow the operating program to define the serial bit rate for the teleprinter.

### Load Paper Tape
Paper Tapes suitable for use with the KIM-1 system are generated using the format shown in Appendix F. To read such a tape into the KIM-1 system, proceed as follows:

1. Load the punched paper tape on to the tape mechanism<br>
2. Type <kbd>L</kbd><br>
3. Activate the paper tape reader

The paper tape will advance and data will be loaded into addresses as specified on the tape. A printed copy of the data read will be generated simultaneously with the reading of the paper tape.

Check-sums are generated during the reading of the paper tape and are compared to check-sums already contained on the tape. A checksum error will cause an error message to appear in the printed copy.

### Punch Paper Tape
The KIM-1 system can be used to punch paper tapes having the format described in Appendix F. The procedures for generating these tapes is as follows:

1. Define the starting address and ending address of the data block to be punched on the paper tape.<br>
2. Load blank paper tape on the punch unit and activate the punch.

| Type | Printer Responds |
|------|------------------|
| <kbd>1</kbd><kbd>7</kbd><kbd>F</kbd><kbd>7</kbd><kbd>SPACE</kbd> | <samp>17F7 xx</samp> |
| <kbd>F</kbd><kbd>F</kbd><kbd>.</kbd> | <samp>17F8 xx</samp> |
| <kbd>0</kbd><kbd>3</kbd><kbd>.</kbd> | <samp>12F9 xx</samp> |
| <kbd>2</kbd><kbd>0</kbd><kbd>0</kbd><kbd>SPACE</kbd> | <samp>0200 xx</samp> |

You have now loaded the ending address (<code class="HEX">0x03FF</code>) into address locations <code class="HEX">0x17F7</code> (EAL) and <code class="HEX">0x17F8</code> (EAH). The starting address (<code class="HEX">0x0200</code>) is selected as shown.

3. Now type <kbd>Q</kbd>

The paper tape will advance snd punching of the data will proceed. Simultaneously, a printed record of the data will be typed.

### List Program
A printed record of the contents of the KIM-1 memory may be typed. The procedure Is the same as for punching paper tape except that the punch mechanism is not activated.

### Execute Program
To initiate execution of a program using the TTY keyboard, the following procedures should be followed:

1. Enter the starting address of the program<br>
2. Type <kbd>G</kbd>

For example, to begin program execution from address location 0200:

| Type | Printer Responds |
|------|------------------|
| <kbd>2</kbd><kbd>0</kbd><kbd>0</kbd><kbd>SPACE</kbd> | <samp>0200 xx</samp> |
| <kbd>G</kbd> | <samp>12F9 xx</samp> |

Program execution begins from, location <code class="HEX">0x0200</code> and will continue until the <kbd>ST</kbd> or <kbd>RS</kbd> keys of the KIM-1 module are depressed. The single step feature may be employed while in the TTY mode.
