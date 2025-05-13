# 0x00-pagination

This directory contains Python modules and scripts that demonstrate various pagination techniques. These techniques are essential for efficiently handling large datasets by breaking them into smaller, manageable chunks. The focus is on implementing both simple and hypermedia pagination methods.

## Files

### 0-simple_helper_function.py
- Contains the `index_range` function, a helper function that calculates the start and end indexes for pagination.

### 1-simple_pagination.py
- Implements a `Server` class that demonstrates simple pagination using the `index_range` function.

### 2-hypermedia_pagination.py
- Extends the `Server` class to include hypermedia pagination.
- Provides additional metadata such as total pages, current page, next page, and previous page.
- Useful for RESTful APIs following HATEOAS principles.

### 3-hypermedia_del_pagination.py
- Further extends the `Server` class to handle deletion-aware pagination.
- Ensures consistent pagination even when items are removed from the dataset.

### Popular_Baby_Names.csv
- A sample dataset used for demonstrating the pagination techniques.
- Contains popular baby names and related data.

## Usage

Each script can be executed independently to test the pagination methods. For example:

```bash
python3 2-main.py
```

This will demonstrate the hypermedia pagination implemented in `2-hypermedia_pagination.py`.

## Learning Objectives

- Understand the concept of pagination and its importance in handling large datasets.
- Learn how to implement simple and hypermedia pagination in Python.
- Explore deletion-aware pagination to maintain consistency in paginated data.

## Author
This project is part of the ALX Backend curriculum.
