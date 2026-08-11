# Appendix F - Paper Tape Forman

The paper tape LOAD and DUMP routines store and retrieve data in a specific format designed to insure error free recovery. Each byte of data to be stored is converted to two half bytes. The half bytes (whose possible values are <code class="HEX">0x0</code> to <code class="HEX">0xF</code> ) are translated into their ASCII equivalents and written out onto paper tape in this form.

Each record outputted begins with a ";" chsiracter (ASCII <code class="HEX">0x3B</code>) to mark the start of a valid record. The next byte transmitted (<code class="HEX">0x18</code>) is the number of data bytes contained in the record. The record's starting address High (1 byte, 2 characters), starting address Lo (1 byte, 2 characters) , and data (24 bytes , 48 characters) follow. Each record is terminated by the record's check-sum (2 bytes, 4 characters), a carriage return (ASCII <code class="HEX">0x0D</code>) , line feed (ASCII <code class="HEX">0x0A</code>) , and six "NULL" characters (ASCII <code class="HEX">0x00</code>).

The last record transmitted has zero data bytes (indicated by ;00). The starting address field is replaced by a four digit Hex number representing the total number of data records contained in the transmission, followed by the records usual check-sum digits. A "XOFF" character ends the transmission.

```
;180000FFEEDDCCBBAAOO99887766554433221122334455667788990AFC
;0000010001
```

During a "LOAD" all incoming data is ignored until a ";" character is received. The receipt of non ASCII data or a mismatch between a records calculated check-sum and the check-sum read from tape will cause an error condition to be recognized by KIM. The check-sum is calculated by adding all data in the record except the ";" character. 

The paper tape format described is compatible with all other MOS Technology, Inc. software support programs.


