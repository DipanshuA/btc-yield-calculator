
---

## 🧪 `amm_sim.py`

```python
# Simple Curve StableSwap (approximation) for BTC/ETH

def curve_swap(x, y, dx, A=100):
    """
    x: reserve of token X (BTC)
    y: reserve of token Y (ETH)
    dx: amount of X being swapped in
    A: amplification coefficient
    """

    D = x + y  # Simplified invariant (not full Curve math)

    new_x = x + dx
    new_y = (D * D) / (4 * new_x)  # Approx of stableswap formula

    dy = y - new_y  # Output ETH

    return new_x, new_y, dy

if __name__ == "__main__":
    btc = 100
    eth = 100
    swap_amount = 1  # Swap 1 BTC

    print(f"Initial Balances: BTC={btc}, ETH={eth}")

    btc, eth, dy = curve_swap(btc, eth, swap_amount)

    print(f"Swap {swap_amount} BTC → ETH returns ≈ {dy:.4f} ETH")
    print(f"New Balances: BTC={btc:.2f}, ETH={eth:.2f}")
