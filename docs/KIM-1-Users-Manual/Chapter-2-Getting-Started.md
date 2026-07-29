# Chapter 2 - Getting Started

This chapter is intended to guide you through the first important steps in achieving initial operation of your KIM-1 Microcomputer Module. We will ask you to perform certain operations without explanation at this time as to why they are being done. In later sections of this manual, full explanations will be offered for every operating procedure.

## Parts complement

After unpacking the shipping container for your KIM-1, you should have located the following items:

* 3 Books - [KIM-1 Users Manual](../kim-1-users-manual.md) 
    * Hardware Manual 
    * Programming Manual
* 1 Programming Card
* 1 System Schematic
* 1 KIM-1 Module 
* 1 Connector (Already mounted on the Module)
* 1 Hardware Packet 
* 1 Warranty Card

You may wish to save the shipping container and packing material should you need to return your KIM-1 module to us at some future date.

## A few words of caution

Your KIM-1 module includes a number of MOS integrated circuits. All such circuits include protective devices to prevent damage resulting from inadvertant application of high voltage potentials to the pins of the device. However, normal precautions should be taken to prevent the appli­ cation of high voltage static discharges to the pins of an MOS device.

Immediately before removal of the packing material from your KIM-1 module, you should develop the following precautionary habits:

1. Discharge any static charge build up on your body by touching a ground connection **before** touching any part of your KIM-1 module. (This precaution is especially important if you are working in a carpeted area)
2. Be certain that soldering irons or test equipment used on the KIM-1 module are properly grounded and not the source of dangerously high voltage levels.

On a different subject, after unpacking your KIM-1 module, you will note the presence of a potentiometer. This adjustment has been set at the factory to insure correct operation of the audio cassette interface circuits. It should **never** be necessary for you to change the position of this potentiometer.

## First Steps

After unpacking the KIM-1 module, locate the small hardware packet and install the rubber pads provided. The rubber pads are located at the bottom of the module (see attached sketch) and act both to lift the card  off your work surface and to provide mechanical support for the module while you depress keys.

Place the module such that the keyboard is to your lower right and observe that two connector locations extend from the module to your left. The connector area on the lower left is referred to as the Application connector (A) . You will note that a 44 pin board edge connector is already installed at this location. The connector area to the upper left is for use by you for future system expansion and is referred to as the Expansion connector (E).

<figure>
    <img src="/img/figure-2.1.png" alt="Figure 2.1 KIM-1 Module">
    <figcaption>Figure 2.1 KIM-1 Module</figcaption>
</figure>

Remove the (A) connector from the module and connect the pins as shown in the sketch.

<figure>
    <img src="/img/figure-2.2.png" alt="Figure 2.2 Power Supply Connections">
    <figcaption>Figure 2.2 Power Supply Connections</figcaption>
</figure>

Reinstall the (A) connector making certain that the orientation is correct.

Note 1: The +12 volt power supply is required only if you will be using an audio cassette recorder in your system. 
Note 2: The jumper from pin A-K to Vss (Pin A-l) is essential for system operation. If you expand your system later, this jumper will be removed and we'll tell you what to do to pin A-K.
Note 3: If you don't have the proper power supplies already available, you may wish to construct the low cost version shown with schematic and parts list in Appendix D. In any event, your power supply **must** be regulated to insure correct system operation and must be capable of supplying the required current levels indicated in the sketch.

Now, recheck your connections, turn on your power supplies, and depress `RS` (reset). You should see the LED display digits light as your first check that the system is operational. If not, recheck your hookup or refer to Appendix C (In Case of Trouble).

## Let's try a simple program

Assuming that you have completed successfully all of the steps thus far, a simple program now can be tried to demonstrate the operation of the system and increase your confidence that everything works properly. We'll be using only the keyboard and display on the module for this example. (In the next two sections we'll worry about the teleprinter and the audio cassette).

For our first example, we will add two 8 bit binary numbers together and display the result. We presume that you are familiar with the hex­ adecimal representation of numbers and the general rules for binary arith­metic.

First check and be sure that the slide switch in the upper right corner of the keyboard is pushed to the left (SST Mode is OFF). Now proceed with the following key sequence:

| Press Keys | See On Display | Step # |
|---|:---:|:---:|
| `AD `| xxxx xx | 1 |
| `0` `0` `0` `2` | 0002 xx | 2 |
| `DA` | 0002 xx | 3 |
| `1` `8` | 0002 18 | 4 |
| `+` `A` `5` | 0003 A5 | 5 |
| `+` `0` `0` | 0004 00 | 6 |
| `+` `6` `5` | 0005 65 | 7 |
| `+` `0` `1` | 0006 01 | 8 |
| `+` `8` `5` | 0007 85 | 9 |
| `+` `F` `A` | 0008 FA | 10 |
| `+` `A` `9` | 0009 A9 | 11 |
| `+` `0` `0` | 000A 00 | 12 |
| `+` `8` `5` | 000B 85 | 13 |
| `+` `F` `B` | 000C FB | 14 |
| `+` `4` `C` | 000D 4C | 15 |
| `+` `4` `F` | 000E 4F | 16 |
| `+` `1` `C` | 000F 1C | 17 |

What you have just done is entered a program and stored it in the RAM at locations `0002` through `000F`. You should have noticed the purpose of several special keys on your keyboard:

| Key | Function |
|------|--------------------------------|
| `AD` | Selects the address entry mode |
| `DA` | Selects the data entry mode |
| `+` | Increments the address without changing the entry mode |
| `0` to `F` | 16 entry keys defining the hex code for address or data entry |

You've noticed as well that your display contains 6 digits. The four on the left are used to display the hex code for an address, the two on the right show the hex code for the data stored at the address shown. Therefore, when you pressed `AD` (step 1) and `0` `0` `0` `2` (step 2), you defined the address entry mode, selected the address 0002, and displayed the address 0002 in the four left-most display digits. Incidentally, when we show an "x" in the display chart, we mean that we don't know what will be displayed and we "don't care."

Next you pressed `DA` (step 3) followed by `1` `8` (step 4). Here, you have defined the data entry mode and entered the value 18 to be stored at your selected address 0002. Of course, the 18 then was dis­played in the two right-most digits of your display.

You remained in the data entry mode but began to press  followed by a two digit number (steps 5 to 17). Note that each depression of the `+` key caused the address displayed to increase by one. The hex keys following the `+` key continued to enter the data field of the display. This procedure is merely a convenience when a number of successive address locations are to be filled.

If you made any mistakes in pressing the keys, you should have noticed that correcting an error is simply a matter of reentering the data until 
the correct numbers show on the display.

The program you have entered is a simple loop to add two 8 bit binary numbers together and present the result on the display. For a programmer, the listing of the program entered might appear as follows:

```asm
POINTL				= $FA
POINTH				= $FB
START				= $1C4F
0000				VAL1
0001				VAL2
0002		18 		PROG		CLC
0003		A5 00			    LDA VAL1
0005		65 01			    ADC VAL2
0007		85 FA			    STA POINTL
0009		A9 00			    LDA #00
000B		85 FB			    STA POINTH
000D		4C 4F 1C			JMP START
```
Stated in simple terms, the program will clear the carry flag (CLC), load VAL1 into the accumulator (LDA VAL1), add with carry VAL2 to the accumulator (ADC VAL2), and store the result in a location POINTL (STA POINTL). A zero value is stored in a location POINTH (LDA #00 and STA POINTH) and the program jumps to a point labelled START (JMP START). This pre-stored program will cause the display to be activated and will cause the address field of your display to show the numbers stored in locations POINTH and POINTL. Note that the result of the addition has already been stored in location POINTL.

The hex codes appearing next to the address field of the listing are exactly the numbers you entered to store the program. We refer to these as machine language codes. For example, 4C is the hex code for the JMP instruction of the microprocessor. The next two bytes of the program define 1C4F (START) as the jump address.

As yet, you are not able to run the program because you have not yet entered the two variables (VAL1 and VAL2). Lets try an actual example:

| Press Keys | See On Display | Step # |
|---|:---:|:---:|
| `AD `| 000F 1C | 17A |
| `0` `0` `F` `1` | 00F1 xx | 17B |
| `DA` `0` `0` | 00F1 00 | 18 |
| `AD` | 00F1 00 | 19 |
| `0` `0` `0` `0` | 0000 xx | 20 |
| `DA` `0` `2` | 0000 02 | 21 |
| `+` `0` `3` | 0001 03 | 22 |
| `+` `GO` | 0002 18 | 23 |

Steps 17A, 17B, and 18 insure that the binary arithmetic mode is selected.

Steps 19 to 21 store the hex value 02 in location 0000 (VAL1). Step 22 stores the hex value 03 in location 0001 (VAL2). Now we are ready to run the program. In step 23, the F°1 key causes the program to execute and the result, 05, appears in the right two digits of the address display. Although the problem appears trivial, it illustrates the basic principles of entering and executing any program as well as providing a fairly high assurance level that your KIM-1 module is operating properly.

You should try one more example using your stored program. Repeat steps 17A to 23 but substitute the value FF for VAL1 and VAL2 at locations 0000 and 0001. Now when you press the I Gol key, your display should read: 

```
00FE xx
```

The answer is correct because:

```
  FF = 1111 1111
+ FF = 1111 1111
  --------------
  FE = 1111 1110
```

Try some more examples if you wish and then let's move on to the rest of the system.

## Adding a tape recorder

In the previous section, you entered and executed a program. If you turn off the power supplies to the system, your program-is lost since the memory into which you stored your program is volatile. If you require the same program again, you would have to repower the system and reenter the program as in the previous example.

The KIM-1 system is designed to work with an audio cassette tape recorder/player to provide you with a medium for permanent storage of your programs or data. The cassette with recorded data may be reread by the system as often as you wish. In this section, you will connect the audio cassette unit to the system and verify its operation.

The recording technique used by the KIM-1 system and the interface circuits provided have been selected to insure trouble-free operation with virtually any type and any quality level audio cassette unit. (We have demonstrated correct operation with a tape unit purchased for less than $20.00 from a local discount outlet). In addition, tapes recorded on one unit may be played back to the system on a different unit if desired. We recommend, of course, that you make use of the best equip­ ment and best quality tapes you have available.

In selecting a tape unit for use with your KIM-1 system, you should verify that it comes equipped with the following features:

1. An earphone jack to provide a source of recorded tape data to the KIM-1 system. <br>
2. A microphone jack to allow recording of data from the KIM-1 system on the tape. <br>
3. Standard controls for Play, Record, Rewind, and Stop. <br>

**Note:** You should avoid certain miniaturized tape equipment intended for dictating applications where the microphone and speaker are enclosed within the unit and no connections are provided to external jacks. If such equipment is used, you will have to make internal modifications to reach the desired connection points.

To connect your tape unit to the KIM-1 module, turn off the power supplies and remove the connector (A) from the module. Add the wires shown in the sketch:

<figure>
    <img src="/img/figure-2.3.png" alt="Figure 2.3 Audio Tape Connections">
    <figcaption>Figure 2.3 Audio Tape Connections</figcaption>
</figure>

Keep the leads as short as possible and avoid running the leads near sources of electrical interference. The connections shown are for typical, portable type units. The Audio Data Out (LO) signal has a level of approx­ imately 15 mv. (peak) at pin M. Should you desire to use more expensive and elaoorate audio tape equipment, you may prefer to connect the high level (1 volt peak) audio signal available at pin P to the "LINE" input of your equipment.

Return the connector (A) to its correct position on the KIM-1 module and turn on the power supplies. To verify the operation of your audio cassette equipment, try the following procedures:

1. Reenter the sample program following the procedures outlined in the previous section (2.4). Try the sample problem again to be sure the system is working correctly. <br>
2. Install a cassette in your tape equipment and REWIND to the limit position. <br>
3. Define the starting and ending address of the program to be stored and assign an identification number (ID) to the program. <br>

| Press Keys | See On Display | Step # |
|---|:---:|:---:|
| `AD `| xxxx xx | 1 |
| `0` `0` `F` `1` | 00F1 xx | 2 |
| `DA` `0` `0` | 00F1 00 | 3 |
| `AD` | 00F1 00 | 4 |
| `1` `7` `F` `5` | 17F5 xx | 5 |
| `DA` `0` `0` | 17F5 00 | 6 |
| `+` `0` `0` | 17F6 00 | 7 |
| `+` `1` `0` | 17F7 10 | 8 |
| `+` `0` `0` | 17F8 00 | 9 |
| `+` `0` `1` | 17F9 01 | 10 |
| `AD` | 1759 01 | 11 |
| `1` `8` `0` `0` | 1800 xx | 12 |

You will recall that the program we wish to store on tape was loaded into locations 0000 to 000F of the memory. Therefore, we define a start­ ing address for recording as 0000 and store this in locations 17F5 and 17F6 (Steps 4 to 7). We define an ending address for recording as one more than the last step of our program and stored the value 0010 (= 000F + 1) in locations 17F7 and 17F8 (Steps 8,9). Finally we pick an arbitrary ID as 01 and store this value at location 17F9 (Step 10).

Note that before we use the audio cassette unit for recording or playing back, we must put 00 in location 00F1 (Steps 1,2 and 3).

The starting address of the tape recording program is 1800. In Steps 11 and 12 we set this address value into the system. If we were to press `GO`, the system would proceed to load data on to the magnetic tape. But first, we'd better start the tape!

4. Select the Record/Play mode of the tape recorder. Wait a few seconds for the tape to start moving and now:

Press `GO`

5. The display will go dark for a short time and then will relight showing:

```
0000 xx
```

6. As soon as the display relights, the recording is finished and you should STOP the tape recorder.

Now, you should verify that the recording has taken place correctly. This can be proven by reading the tape you have just recorded. Procees as follows:

1.   Rewind the tape cassette to its starting position. <br>
2.   Turn off the system power supplies and then later, turn them back on.

This has the effect of destroying your previously stored program which you already have recorded on tape. 

3. Prepare the system for reading the tape as follows:

| Press Keys | See On Display | Step # |
|---|:---:|:---:|
| `RS `| | |
| `AD` | xxxx xx | 1 |
| `0` `0` `F` `1` | 00F1 xx | 2 |
| `DA` `0` `0` | 00F1 00 | 3 |
| `AD` | 00F1 00 | 4 |
| `1` `7` `F` `9` | 17F9 xx | 5 |
| `DA` | 17F9 xx | 6 |
| `0` `1` | 17F9 01 | 7 |
| `AD` | 17F9 01 | 8 |
| `1` `8` `7` `3` | 17F3 xx | 9 |
| `GO` | (Dark) | 10 |

The KIM-1 system is now looking for tape input data with the ID label 01. Recall that this is the same ID label we assigned when we recorded the program.

4. If your tape unit has a volume control, set the control at approximately the half way point. <br>
5. If your tape unit has a tone control, set the control for maximum treble. <br>
6. Now, turn on the tape using the PLAY mode. The tape will move forward and the system will accept the recorded data. As soon as the data record (ID=01) has been read, the display should relight showing:

```
0000 xx
```

You may now stop the tape unit. If the display relights and shows:

```
FFFF xx
```

this means that the selected record has been located and read but that an error has occurred during the reading of the data. In this case, press the B key and repeat the read tape procedures from the beginning. If the `FFFF` still shows on the display, repeat the entire recording and play­ back procedures checking each step carefully. If the problem persists, refer to [Appendix C, (In Case of Trouble)](Appendix-C-In-Case-Of-Trouble.md).

If the tape continues to run and the display does not relight, this means that the system has been unsuccessful in reading any data back from the tape. In this case, repeat the entire recording and playback proce­dures checking each step carefully. If the problem persists, refer to [Appendix C, (In Case of Trouble)](Appendix-C-In-Case-Of-Trouble.md).

7. Assuming that you have read the tape successfully, you now may verify that the program has been restored to memory by trying a sample problem. (02 + 03 = 05)

## Adding a Teleprinter

If you have access to a serial teleprinter, you may add such a unit to the KIM-1 system with very little effort. One of the more commonly available units of this type is the Teletype Model 33ASR which we will use for the purposes of illustration in this section. However, if you have available different equipment, you may use the information presented here as a guide to connecting your specific unit. In any case, we recom­ mend you follow the directions offered by the equipment manufacturer in his instruction manual to effect the desired wiring and connection options.

The KIM-1 provides for a 4 wire interface to the TTY. Specifically, the "20 MA loop" configuration should be used and you should check that your TTY has been wired for this configuration. If not, you may easily change from "60 MA loop" to "20 MA loop" configurations following the manufacturers directions. The KIM-1 has been designed to work properly only with a teleprinter operating in full duplex mode. Check the literature supplied with your teleprinter if you are unsure if your unit is properly configured. You are not restricted to units with specific bit rates (10 CPS for TTY) since the KIM-1 system automatically adjusts for a wide variety of data rates (10CPS, 15CPS, 30CPS, etc.).

To connect the TTY to the system, proceed as follows:

1. Turn off system power and remove connector (A) from the module. <br>
2. Add the wires shown in the sketch to connector (A) and to the appropriate connector on the TTY unit. <br>

<figure>
    <img src="/img/figure-2.4.png" alt="TTY Connections">
    <figcaption>Figure 2.4 TTY Connections</figcaption>
</figure>

3.   The jumper wire from A-21 to A-V is used to define for the KIM-1 system that a teleprinter will be used as the **only** input/display device for the system. If you expect to use both TTY **and** the KIM-1 keyboard/display, you should install the switch shown instead of the jumper. Now, the switch, when open, will allow use of the keyboard and display on the KIM-1 module and, when closed, will select the tele­ printer as the input/display device. (Of course, you may use a clip-lead instead of the switch if you desire). <br>
4.    Be sure pins A-21 and A-V are connected, Reinstall connector (A) and return power to the system. Turn-on the TTY. <br>
5. Press the `RS` key on the KIM-1 module then press the `RUB OUT` key on the TTY. This step is most important since the KIM-1 system adjusts automatically to the bit rate of the serial teleprinter and requires this first key depression to establish this rate.

If everything is working properly you should immediately observe a message being typed as follows:

```
KIM
```

This is a prompting message telling you that the TTY is on-line and the KIM-1 system is ready to accept commands from the TTY keyboard. 

This is a prompting message telling you that the TTY is on-line and the KIM-1 system is ready to accept commands from the TTY keyboard. 

Should the prompting message not be typed press the `RS` key on the KIM-1 keyboard and then the `RUB OUT` key on the TTY. If the "KIM" message still is not typed, recheck all connections and the TTY itself and the TTY itself and then try again. If the problem persists, refer to [Appendix C, (In Case of Trouble)](Appendix-C-In-Case-Of-Trouble.md).

6. Assuming that the TTY is operable, you may now try a simple group of operations to verify correct system operation:

| Press Keys | See Printed | Step # |
|---|---|:---:|
| | KIM <br> xxxx xx | 1 |
| `0` `0` `0` `2` | 0002 | 2 |
| `SPACE` | 00F1 xx | 3 |
| `1` `8` `•`  | 18. | 4 |
| | 0003 xx | 5 |
| `A` `5` `•` | A5. | 6 |
| | 0004 xx | 7 |
| `LF` | 0003 A5 | 8 |
| `RUB OUT` | KIM <br> xxxx xx | 9 |

Step 1 shows the "KIM" prompting message. In Step 2, an address (0002) is selected followed by a space key in Step 3. The address cell 0002 together with the data stored at that location (xx) is printed. Step 4 shows the "modify cell" operation using the `•` key and the hex data keys preceding. Step 5 shows the incrementing to the next address cell (0003) after the `•` key. Note that the modification of cell 0002 also occurs. Steps 6 and 7 show the modification of data in cell 0003 and the incrementing to cell 0004. Step 8 shows the action of the `LF` key in backing up one cell to 0003 where we can see from the printout that the correct data (A5) has been stored at that location. Step 9 shows the reaction to the `RUB OUT` key in resetting the system and producing a new "KIM" prompting message. Note, by the way, that in this example you have repeated a portion of the program entry exactly as you did in Section 2.4 but this time using the TTY.

So much for now! If all of the operations have occurred properly, you may be certain that your TTY and KIM-1 module are working together correctly. We will describe in detail all of the other operations pos­sible with the TTY in a later section of the manual.

If you have reached this point without problems, you now have completed all of the required system tests and may be confident that the KIM-1 module and your peripheral units are all working correctly. Our next task is to learn more about the KIM-1 system and its operating programs.
