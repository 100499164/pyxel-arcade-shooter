<h1 align="center">1942 Arcade Shooter</h1>

<p align="center"> A 1942-inspired arcade shoot 'em up developed in <strong>Python</strong> using the <strong>Pyxel</strong> game engine. </p>

<p align="center"> <img src="docs/gameplay.png" alt="1942 Arcade Shooter gameplay" width="420"> </p>

## About

This project was originally developed in 2022 as part of a university programming course and is inspired by Capcom's 1942.

It recreates the core gameplay of classic vertical-scrolling arcade shooters, including multiple enemy types, projectile-based combat, power-ups, progressive waves and a scoring system.

## Features

* Object-oriented implementation of players, enemies and projectiles.

* Multiple enemy types with different movement and attack behaviours.

* Five progressively more difficult enemy waves.

* Player and enemy projectile systems.

* Collision detection between players, enemies, bullets and power-ups.

* Dodge mechanic with limited uses.

* Different power-ups that can:

  * Increase the player's score.

  * Increase movement speed.

  * Grant an additional dodge.

  * Grant an additional life.

* Player lives and scoring system.

* High-score tracking during the current execution.

* Sprite-based animations for movement, impacts and explosions.

* Scrolling background inspired by the original \*1942\* arcade game.




## Controls

<p>
  <kbd>↑</kbd> <kbd>↓</kbd> <kbd>←</kbd> <kbd>→</kbd>
  &nbsp; Move the aircraft
</p>

<p>
  <kbd>Space</kbd>
  &nbsp; Shoot
</p>

<p>
  <kbd>Z</kbd>
  &nbsp; Perform a dodge
</p>

<p>
  <kbd>Q</kbd>
  &nbsp; Quit the game
</p>

<p>
  <kbd>R</kbd>
  &nbsp; Restart after Game Over
</p>

## Requirements

* Python 3.11 or later
* Pyxel 2.9.6



Install the project dependencies using:



```bash

pip install -r requirements.txt

```



## Running the Game



Clone the repository and navigate to its directory:



```bash

git clone https://github.com/100499164/1942-pyxel.git

cd 1942-pyxel

```



Install the required dependencies:



```bash

pip install -r requirements.txt

```



Then run:



```bash

python main.py

```



## Project Structure

```text
.
├── Assets/
│   └── banco_general.pyxres
├── docs/
│   └── gameplay.png
├── avion.py
├── bala.py
├── balaEnemigo.py
├── balaPlayer.py
├── board.py
├── config.py
├── enemigo.py
├── enemigoBombardero.py
├── enemigoRegular.py
├── enemigoRojo.py
├── enemigoSuperbombardero.py
├── main.py
├── player.py
├── powerup.py
└── requirements.txt
```

## Development

This repository contains the original university project together with later maintenance, bug fixes and refactoring improvements aimed at improving code quality and maintainability.

## Disclaimer & Copyright

This is a **non-commercial, academic project** created strictly for educational, portfolio, and demonstrative purposes. 

* **Codebase:** All python scripts (`.py` files) and structural logic are original work.
* **Visual Assets:** The `banco_general.pyxres` file includes original sprite sheets and graphics extracted from the classic **1942** arcade game (1984), which is a registered trademark and intellectual property of **Capcom Co., Ltd.**
* **Fair Use:** This project is not endorsed by, affiliated with, or linked to Capcom. Resource usage qualifies under "Fair Use" guidelines for academic review and non-profit educational purposes. 

*If you are a copyright representative for Capcom and wish to have the original visual assets removed from this educational repository, please open an Issue or contact me directly, and they will be promptly replaced with generic shapes.*
