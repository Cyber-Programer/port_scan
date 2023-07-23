
![Logo](https://i.postimg.cc/3J3G4jL0/Designer-e-Bay-Logo.png)


# Port scanner - Website Port Scanner

Discover open ports on any website effortlessly. Enhance security and fortify defenses with PortScanWeb. A must-have tool for security researchers and web administrators.
## How does this tool work

This tool was written in python language


This tool was using some python modules

You need to install python in your system

#### Modules :
 `argparse `,`socket`,`threading `,`time`.Thos modules are using hear
## Features
- Web open port scanning
- port rang (custom)
- Using thread (custom)
- verbose mode (optional)
- Super first output

## Follow this for a better user experience

This project was made using Python:

- First, ensure you have `python` installed.

Follow these steps:

- `-p` or `--start-port`: Specify the starting port for the range.

- `-ep` or `--end-port`: Specify the ending port for the range.

- `-t` or `--thread`: Enable threading [By default, the number of threads is set to 500. You can increase the threading value according to your system's processing power if you want to get output faster].

- `-v` or `--verbose`: Enable verbose output.

## Tool look like...

```python
          _                                   _
  __ _  _| |__  ___ _ _   ___   _ __  ___ _ _| |_ ___ __ __ _ _ _  _ _  ___ _ _
 / _| || | '_ \/ -_) '_| |___| | '_ \/ _ \ '_|  _(_-</ _/ _` | ' \| ' \/ -_) '_|
 \__|\_, |_.__/\___|_|         | .__/\___/_|  \__/__/\__\__,_|_||_|_||_\___|_|
     |__/                      |_|


usage: port_scanner.py [-h] [-p] [-ep] [-t] [-v] Target IP
te.py: error: the following arguments are required: Target IP
```


## Authors

- [@Cyber-Programer](https://www.github.com/Cyber-Programer)


## Run &#8595;

#### First install python in your system
.

Clone my tool:

```bash
  git clone https://github.com/Cyber-Programer/port_scan.git
```

Go to the project directory

```bash
  cd port_scan
```

Install requirements

```bash
  pip install -r requirements.txt
```

Start the tool

```bash
  python3 port_scanner.py
```


## Screenshots

### starting 
![App Screenshot](https://i.postimg.cc/d03PLdY2/Capture.png)

### port found
![Port found](https://i.postimg.cc/DyQcRyNL/Capture2.png)
