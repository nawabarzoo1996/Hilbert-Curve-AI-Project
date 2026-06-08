# Hilbert Curve Generator & Visualizer

A simple program that **generates and draws** a Hilbert space-filling curve
of any order, and shows the 1D → 2D mapping numerically.

---

## What it does

- Generates the points of a Hilbert curve for any order using the `d2xy()` function
- Draws the curve as a single continuous line, coloured from start (teal) to end (purple)
- Shows how the curve grows as the order increases
- Prints the actual distance → (x, y) mapping so you can see the math

---

## How to run

1. Install libraries:
   ```
   pip install numpy matplotlib
   ```
2. Run it:
   ```
   python hilbert_generator.py        # draws orders 1-4 + a detailed order-6 curve
   python hilbert_generator.py 5      # draws a single curve of the order you choose
   ```
3. Check the generated `.png` files.

---

## How it works (the key function)

```python
def d2xy(n, d):
    # n = grid side (must be a power of 2)
    # d = distance along the curve (0 to n*n - 1)
    # returns the (x, y) position in the grid
```

The curve is built by walking distance `d` from 0 upward, and for each `d`
computing where that point sits in the 2D grid. Bit operations and quadrant
rotations create the recursive, self-similar shape.

---

## Outputs

- `hilbert_orders.png` — orders 1, 2, 3, 4 side by side (shows growth)
- `hilbert_big.png` — a detailed order-6 curve (4096 points)
- `hilbert_order_N.png` — a single curve when you pass an order number

The colour flows from start to end, proving it is **one continuous line**.

---

## Example mapping (order 2, a 4×4 grid)

| distance d | (x, y) |
|-----------|--------|
| 0 | (0, 0) |
| 1 | (1, 0) |
| 2 | (1, 1) |
| 3 | (0, 1) |
| ... | ... |
| 15 | (3, 0) |

Notice how consecutive `d` values land on **neighbouring** cells — that is the
**locality preservation** property in action.

---

## Concepts demonstrated (for the AI course)

- **Space-filling curve** — one line covering a whole 2D area
- **Recursive / fractal** structure — same pattern at every scale
- **1D ↔ 2D mapping** — the `d2xy` function
- **Locality preservation** — nearby distances map to nearby positions
