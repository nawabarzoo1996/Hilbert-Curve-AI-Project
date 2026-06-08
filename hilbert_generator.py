"""
=================================================================
HILBERT CURVE GENERATOR & VISUALIZER
=================================================================
A simple program that generates and draws a Hilbert space-filling
curve of any order.

Run:
    python hilbert_generator.py          # draws orders 1-4 + a big one
    python hilbert_generator.py 5        # draws a single curve of order 5

Concept: a Hilbert curve fills a 2D square with one continuous line.
Higher order = more detail. Built using the d2xy() mapping function.
=================================================================
"""
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# ----------------------------------------------------------------
# CORE: map a distance d along the curve to an (x, y) grid position
# ----------------------------------------------------------------
def d2xy(n, d):
    """n = grid side (power of 2), d = distance along curve (0..n*n-1)."""
    rx = ry = 0
    x = y = 0
    t = d
    s = 1
    while s < n:
        rx = 1 & (t // 2)
        ry = 1 & (t ^ rx)
        if ry == 0:                       # rotate the quadrant
            if rx == 1:
                x = s - 1 - x
                y = s - 1 - y
            x, y = y, x
        x += s * rx
        y += s * ry
        t //= 4
        s *= 2
    return x, y

def hilbert_points(order):
    """Return the list of (x, y) points that make up a Hilbert curve."""
    n = 2 ** order
    return [d2xy(n, d) for d in range(n * n)]

# ----------------------------------------------------------------
# DRAW a single curve, coloured along its length (start -> end)
# ----------------------------------------------------------------
def draw_curve(order, ax):
    pts = hilbert_points(order)
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    # build coloured segments so we can see the path direction
    points = np.array([xs, ys]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    lc = LineCollection(segments, cmap="viridis", linewidth=2)
    lc.set_array(np.linspace(0, 1, len(segments)))
    ax.add_collection(lc)
    ax.plot(xs[0], ys[0], "o", color="#0E7C7B", markersize=7)   # start
    ax.plot(xs[-1], ys[-1], "s", color="#8B5CF6", markersize=7)  # end
    ax.set_xlim(-1, 2 ** order)
    ax.set_ylim(-1, 2 ** order)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(f"Order {order}  ({len(pts)} points)", fontsize=11)

# ----------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------
def main():
    if len(sys.argv) > 1:
        # single curve of the requested order
        order = int(sys.argv[1])
        fig, ax = plt.subplots(figsize=(6, 6))
        draw_curve(order, ax)
        plt.suptitle(f"Hilbert Curve — Order {order}", fontsize=14, fontweight="bold")
        out = f"hilbert_order_{order}.png"
        plt.savefig(out, dpi=120, bbox_inches="tight")
        print(f"Saved {out}")
        # print some facts
        n = 2 ** order
        print(f"Grid size : {n} x {n}")
        print(f"Points    : {n*n}")
        print(f"Curve length (steps): {n*n - 1}")
    else:
        # progression of orders 1-4
        fig, axes = plt.subplots(1, 4, figsize=(16, 4))
        for i, order in enumerate([1, 2, 3, 4]):
            draw_curve(order, axes[i])
        plt.suptitle("Hilbert Curve — Growing Through Orders", fontsize=15, fontweight="bold")
        plt.tight_layout()
        plt.savefig("hilbert_orders.png", dpi=120, bbox_inches="tight")
        print("Saved hilbert_orders.png")

        # one big detailed curve
        fig, ax = plt.subplots(figsize=(7, 7))
        draw_curve(6, ax)
        plt.suptitle("Hilbert Curve — Order 6 (4096 points)", fontsize=14, fontweight="bold")
        plt.savefig("hilbert_big.png", dpi=120, bbox_inches="tight")
        print("Saved hilbert_big.png")

    # demonstrate the mapping numerically
    print("\nExample mapping (order 2, 4x4 grid):")
    print("distance d -> (x, y) position")
    for d in range(16):
        x, y = d2xy(4, d)
        print(f"  d={d:>2}  ->  ({x}, {y})")

if __name__ == "__main__":
    main()
