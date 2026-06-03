# Python Turn-Based RPG

A turn-based CLI RPG combat system built in Python using Object-Oriented Programming (OOP) principles.

This project was created primarily as a learning project to practice Python, OOP design, game programming concepts, and software architecture. While it runs entirely in the command line, the underlying systems were designed to be reusable and potentially adapted to a future game engine such as Godot.

## Features

### Combat System
- Turn-based battle loop
- Player vs Enemy combat
- Health and stamina management
- Win/Loss conditions
- Run Away option

### Actions
- Attack
- Heal
- Defend
- Stamina Recovery

### Character Systems
- Health and maximum health tracking
- Stamina and maximum stamina tracking
- Temporary defending state
- Damage mitigation while defending

### Enemy AI
- Random action selection
- State-aware action filtering
- Prevents healing at full health
- Prevents stamina recovery at full stamina
### Menu System
- Main menu
- Start game option
- Exit option
- Return to menu by running away from battle

## Project Structure
'''text
main.py
│
├── Menu Flow
└── Game Startup

game_engine.py
│
├── Battle Loop
├── Player Turn Logic
├── Enemy Turn Logic
└── Status Display

character.py
│
├── Character Stats
├── Health Management
├── Stamina Management
└── State Management

action.py
│
├── Base Action Class
├── Attack Action
├── Heal Action
├── Defend Action
└── Stamina Recovery Action
'''

## Programming Concepts Practiced
### Python
- Classes and Objects
- Inheritance
- Encapsulation
- Methods
- Lists
- Loops
- Conditional Logic
- Error Handling
- Return Values

### Game Programming
- Action systems
- State management
- Resource management
- Basic AI decision-making
- Combat architecture
- Menu and game flow design

## Learning Goals

This project was built to:

- Practice Object-Oriented Programming in Python
- Learn how game mechanics can be structured in code
- Explore game architecture without relying on a game engine
- Build reusable gameplay systems
- Prepare for future game development in Godot

## Current Status

### Learning Project Complete

The project has achieved its original learning objectives and serves as a working example of a turn-based combat system.

The repository remains open as a sandbox for experimenting with future gameplay systems and game programming concepts.


