# 0x01-caching

This directory contains Python projects and exercises related to caching systems, as part of the ALX Backend curriculum.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Files](#files)
- [Author](#author)

## Description

The goal of this project is to explore the concepts of caching, and how to implement different caching strategies in Python. The project covers several caching mechanisms including:
- Basic caching
- FIFO (First In First Out) caching
- LIFO (Last In First Out) caching
- LRU (Least Recently Used) caching
- MRU (Most Recently Used) caching

These strategies are implemented as Python classes, allowing for easy integration and testing.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/hassanah391/alx-backend.git
   ```
2. Navigate to this directory:
   ```bash
   cd alx-backend/0x01-caching
   ```
3. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

## Usage

Each caching strategy is implemented in its own Python file as a class. You can import and use these classes in your own Python scripts or run the example scripts provided.

Example usage:
```python
from base_caching import BaseCaching
from basic_cache import BasicCache

my_cache = BasicCache()
my_cache.put("item1", "value1")
print(my_cache.get("item1"))
```

## Files

- `base_caching.py`: Defines the base class for all caching systems.
- `basic_cache.py`: Implements a simple caching system with no limit.
- `fifo_cache.py`: Implements First-In-First-Out caching.
- `lifo_cache.py`: Implements Last-In-First-Out caching.
- `lru_cache.py`: Implements Least-Recently-Used caching.
- `mru_cache.py`: Implements Most-Recently-Used caching.
- Additional files for tasks and tests may be present.

## Author

- hassan ahmed: <hassan.ahmed357753@gmail.com>