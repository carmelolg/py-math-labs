# python
import math
import time
import argparse

# Costante dei primi gemelli C2 (valore noto numerico)
C2 = 0.6601618158468695739278

# Crivello di Eratostene
def sieve_primes(limit):
    # Restituisce un bytearray di lunghezza limit+1 con 1 per i numeri primi e 0 per i composti
    if limit < 2:
        return bytearray()
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            step = p
            # calcola quante celle devono essere sovrascritte e assegna zeri in blocco
            sieve[start : limit + 1 : step] = b"\x00" * (((limit - start) // step) + 1)
    return sieve

def brun_partial(limit):
    sieve = sieve_primes(limit + 2)  # +2 to test p+2
    s = 0.0
    count = 0
    for p in range(2, limit - 1):
        if sieve[p] and sieve[p + 2]:
            s += 1.0 / p + 1.0 / (p + 2)
            count += 1
    return s, count

def estimate_tail(limit):
    """
    Stima la coda della somma dei reciproci dei primi gemelli oltre `limit`.
    Restituisce 0.0 per limit < 3, altrimenti 4*C2 / ln(limit).
    """
    if limit < 3:
        return 0.0
    return 4.0 * C2 / math.log(limit)

def main():
    parser = argparse.ArgumentParser(description="Stima della costante di Brun per primi gemelli")
    parser.add_argument("--limit", "-n", type=int, default=1_000_000,
                        help="Calcola sommando i primi gemelli fino a questo limite (default 1_000_000)")
    args = parser.parse_args()

    limit = args.limit
    t0 = time.time()
    partial_sum, count = brun_partial(limit)
    tail = estimate_tail(limit)
    total_estimate = partial_sum + tail
    dt = time.time() - t0

    print(f"Limite: {limit}")
    print(f"Gemelli trovati: {count}")
    print(f"Somma parziale  S(N): {partial_sum:.12f}")
    print(f"Stima coda    ~4*C2/ln(N): {tail:.12f}")
    print(f"Stima totale  S(N)+coda: {total_estimate:.12f}")
    print(f"Tempo: {dt:.2f}s")

if __name__ == "__main__":
    main()