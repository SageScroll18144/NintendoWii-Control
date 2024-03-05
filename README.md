# IHS Project
This project runs a Python application on a DE2i-150 FPGA and is part of discipline IF817(Hardware-Software Interface).

The python application simulates a Playstation 2 interface and runs some classic games with with a own develop Nintendo Wii controller.

## Content

- [Apps Docs](apps/README.md)
- [FPU Docs](FPU/)
- [Nintendo Wii Control Docs](control/)
- [DE2i-150 FPGA Drive](drive/)

## Project tree

    .
    ├── FPU
    │   ├── device_state
    │   │   └── device_state.h
    │   ├── interface_app
    │   │   ├── socket_react.c
    │   │   └── socket_react.h
    │   ├── receive_es
    │   │   └── EStoAPP.py
    │   ├── run
    │   │   └── main.c
    │   ├── serial
    │   │   └── run.sh
    │   └── platformio.ini
    ├── apps
    │   ├── images
    │   │   └── *
    │   ├── src
    │   │   └── *
    │   ├── video
    │   │   └── intro.mp4
    │   ├── README.md
    │   ├── emulator_apps-1.1.0-py3-none-any.whl
    │   ├── menu.py
    │   └── requirements.txt
    ├── control
    │   ├── include
    │   │   └── README.md
    │   ├── lib
    │   │   └── *
    │   ├── src
    │   │   └── main.cpp
    │   ├── test
    │   │   └── README.md
    │   └── platformio.ini
    ├── driver
    ├── char
    │   ├── dummy.c
    │   └── Makefile
    └── pci
        ├── de2i-150.c
        └── Makefile
    ├── CODE_OF_CONDUCT.md
    └── README.md



## How to run the project


## Group

- [Felipe Santos (ffss)](https://github.com/SageScroll18144)
- [José Daniel (jdsc2)](https://github.com/JDaniielC)
- [Lorenzo (lfc4)](https://github.com/)
- [Lucas Emmanuel (legl)](https://github.com/OhLK)
- [Lucas Monterazo (lsm6)](https://github.com/Monterazo)
- [Luís Trevisan (lpst)](https://github.com/luis-trevisan)
