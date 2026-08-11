# Contributing

Thank you for your interest in contributing to this project! Please follow these formatting guidelines when submitting contributions.

## Formatting Guidelines

### Physical Keys
Use the `<kbd>` HTML tag for physical keys:
```html
<kbd>GO</kbd>
```

### Hexadecimal Values
Use a code tag with the `hex` class for visual distinction:
```html
<code class="hex">0xFF</code>
```

### Code, Mnemonics, and Instructions
Use inline backticks for code, mnemonics, and instruction names:
```
`memset`
`MOV`
`ADD`
```

For longer code blocks, use triple backticks with the `asm` language tag:
````
```asm
MOV A, B
ADD A, 0x10
```
````

### Machine Output and Screen Display
Use the `<samp>` HTML tag for machine output and what appears on screen:
```html
<samp>READY</samp>
<samp>ERROR: Invalid input</samp>
```

## Rendering

This project uses ReadTheDocs (RTD) for documentation rendering. All HTML tags (`<kbd>`, `<code class="hex">`, `<samp>`) will render inline and style appropriately in the documentation build.

## Example

Here's how these guidelines work together in practice:

Press <kbd>ENTER</kbd> to initialize. The system will respond with <samp>READY</samp>. To set a memory address to the value <code class="hex">0xFF</code>, use the `memset` instruction as follows:

```asm
memset 0x1000 0xFF
```

---

Thank you for helping improve our documentation!
