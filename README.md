# Hexdoku - SAINTCON Hackers Challenge 2024

A hexadecimal Sudoku puzzle game built as a CTF challenge for SAINTCON's Hackers Challenge 2024.

## Overview

Hexdoku is a Sudoku variant where the puzzle behavior is controlled by environment variables. The application supports three difficulty levels:

- **Small (4x4)** - Uses digits 1-4, with 2x2 sub-boxes
- **Medium (9x9)** - Uses digits 1-9, with 3x3 sub-boxes
- **Large (16x16)** - Uses hex values 0-9 and a-f, with 4x4 sub-boxes

Each level has pre-filled constraint cells and a unique flag revealed upon solving.

## Available Levels

| Level | Env File | Grid Size | Constraints |
|-------|----------|-----------|-------------|
| Small 1 | `.env-s-1` | 4x4 (16 cells) | 2 |
| Small 2 | `.env-s-2` | 4x4 (16 cells) | 3 |
| Small 3 | `.env-s-3` | 4x4 (16 cells) | 4 |
| Medium 1 | `.env-m-1` | 9x9 (81 cells) | 21 |
| Medium 2 | `.env-m-2` | 9x9 (81 cells) | 21 |
| Medium 3 | `.env-m-3` | 9x9 (81 cells) | 24 |
| Large 1 | `.env-l-1` | 16x16 (256 cells) | 140+ |
| Large 2 | `.env-l-2` | 16x16 (256 cells) | 140+ |

## Running Locally with Docker

### Prerequisites

- Docker
- Docker Compose

### Steps

1. Choose a level and copy its env file to `.env`:
   ```bash
   # Small puzzle (easiest)
   cp .env-s-1 .env

   # Medium puzzle
   cp .env-m-1 .env

   # Large puzzle (hardest)
   cp .env-l-1 .env
   ```

2. Start the application:
   ```bash
   docker compose -f docker-compose-local.yml up
   ```

3. Access the game at: http://127.0.0.1:8000

4. To stop:
   ```bash
   docker compose -f docker-compose-local.yml down
   ```

### Switching Levels

To switch to a different level:
1. Stop the containers (`Ctrl+C` or `docker compose -f docker-compose-local.yml down`)
2. Copy a different env file to `.env`
3. Restart the application

## How to Play

1. Fill in the grid so that each **row**, **column**, and **sub-box** contains unique values
2. Valid values depend on the difficulty:
   - Small: `1`, `2`, `3`, `4`
   - Medium: `1` through `9`
   - Large: `0` through `9` and `a` through `f`
3. Gray cells are **constraints** - pre-filled values that cannot be changed
4. Navigation:
   - Use arrow keys or Tab to move between cells
   - Constraint cells are automatically skipped
5. Click **Submit** when complete to validate your solution
6. A correct solution reveals the flag

## Solution References

Solution images for each puzzle are available in the `/solutions/` directory:
- `solution-s-1.png` through `solution-s-3.png` (Small)
- `solution-m-1.png` through `solution-m-3.png` (Medium)
- `solution-l-1.png` and `solution-l-2.png` (Large)
