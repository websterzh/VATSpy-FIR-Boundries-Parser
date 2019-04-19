# VATSpy-FIR-Boundries-Parser
A simple parser to convert all fir boundries defined in VATSpy to json format.

## Running Environment
+ Python 3

## Default Configuration
+ INPUT_FILE - Location of input file, defaultly ```./FIRBoundaries.dat```
+ OUTPUT_FILE - Location of output file, defaultly ```./out.json```
+ IDENT - Define this to beautify the output json. This can be ```None``` or a ```integer```, defaultly ```None```

## VATSpy
VAT-Spy is a simple application that allows you to view current ATC staffing and traffic levels on VATSIM. For more information please check [Here](http://www1.metacraft.com/VATSpy/).

## Sample Input
```
ANAU|0|0|7|-11.800000|160.000000|3.500000|170.000000|-4.150000|165.000000
3.500000|160.000000
3.500000|170.000000
-10.000000|170.000000
-11.800000|166.875000
-10.500000|166.750000
-4.833333|160.000000
3.000000|160.000000
```

## Sample Output
*Example below using INDENT = 2*
```
[
  {
    "ident": "ANAU",
    "boundaries": [
      {
        "lat": "3.500000",
        "lon": "160.000000"
      },
      {
        "lat": "3.500000",
        "lon": "170.000000"
      },
      {
        "lat": "-10.000000",
        "lon": "170.000000"
      },
      {
        "lat": "-11.800000",
        "lon": "166.875000"
      },
      {
        "lat": "-10.500000",
        "lon": "166.750000"
      },
      {
        "lat": "-4.833333",
        "lon": "160.000000"
      },
      {
        "lat": "3.000000",
        "lon": "160.000000"
      }
    ]
  }
]
```