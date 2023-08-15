from test_framework import generic_test


def reverse_bits(x: int) -> int:
    # Brute Force solution since book asks did look up of every 16 bit word combo (>5000 lines)
    for i in range(32):
        x = swap_bits(x,i,(63-i))
    return x

def swap_bits(x, i, j):
    # Check if Bits at i and J are different and needed to be switched
    if (x >> i) & 1 != (x >> j) & 1:
        bit_mask = (1 << i) | (1 << j)  # Bit Mask - to Help Swap Creates a number with 1 in the swap position
        x ^= bit_mask # XOR with Bit Mask - 1s are in swap position so if org was 1 -> 0
    return x

if __name__ == '__main__':
    
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
    