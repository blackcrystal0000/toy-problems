## Toy Problem Solutions

## This repository contains the Python solutions for the following toy problems:

1. Converting 12-hour time to 24-hour time
2. Two numbers are positive.
3. Consonant value

To run the solutions, simply run the Python files in your preferred environment.

## Challenge 1: Converting 12-hour time to 24-hour time

The function `convert_to_24hour(hour: int, minute: int, period: str) -> str` takes an hour (between 1 and 12), a minute (between 0 and 59), and a period (either "am" or "pm") as input. It returns a four-digit string that encodes that time in 24-hour time.

## Example usage:

```
>>> convert_to_24hour(8, 30, "am")
'0830'
>>> convert_to_24hour(8, 30, "pm")
'2030'
```

## Challenge 2: Two numbers are positive.

The function `two_positive(a: int, b: int, c: int) -> bool` takes three integers as input (a, b, and c). It returns True if exactly two out of the three integers are positive numbers (greater than zero), and False otherwise.

## Example usage:

```
>>> two_positive(2, 4, -3)
True
>>> two_positive(-4, 6, 8)
True
>>> two_positive(4, -6, 9)
True
>>> two_positive(-4, 6, 0)
False
>>> two_positive(4, 6, 10)
False
>>> two_positive(-14, -3, -4)
False
```

## Challenge 3: Consonant value

The function `consonant_value(s: str) -> int` takes a lowercase string that has alphabetic characters only and no spaces as input. It returns the highest value of consonant substrings. Consonants are any letters of the alphabet except "aeiou". We assign the following values: a = 1, b = 2, c = 3, .... z = 26.

## Example usage:

```
>>> consonant_value("zodiacs")
26
>>> consonant_value("strength")
57
```

Note: in the second example, we cross out the vowels to get "str" and "ngth". The values of these substrings are "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49. The highest value is 57.

Enjoy solving these toy problems!

## Author
Crystal Kariuki. 

## License
MIT License

Copyright (c) 2023 blackcrystal0000

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

This is licensed by MIT license
