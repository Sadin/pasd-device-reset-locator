from __future__ import annotations

import sys

import pandas as pd

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise ValueError(
            'application requires 2 filepaths for input,' +
            'Prime CSV path followed by Intune CSV path.')

    primePath = sys.argv[1]
    intunePath = sys.argv[2]

    primeData = pd.read_csv(primePath)
    intuneDada = pd.read_csv(intunePath)

    print(f'Prime(wireless): {primePath}')
    print(f'Endpoint(Intune): {intunePath}')
