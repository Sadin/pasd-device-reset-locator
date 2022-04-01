from __future__ import annotations

import sys

import pandas as pd


def csvcheck(filename: str) -> bool:
    if filename.rpartition('.')[2] != 'csv':
        return False
    return True


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise ValueError(
            'application requires 2 filepaths for input,' +
            'Prime CSV path followed by Intune CSV path.')

    paths = (sys.argv[1].strip(), sys.argv[2].strip())

    if not csvcheck(paths[0]) or not csvcheck(paths[1]):
        raise ValueError('One of the files is not a csv')

    # import CSVs from input paramaters as dataframes
    # prime data has header information that can be ignored,
    # start import at row index 8
    primeData = pd.read_csv(paths[0], header=8)
    intuneDada = pd.read_csv(paths[1])

    # print paths for debug
    print(f'Prime(wireless): {paths[0]}')
    print(f'Endpoint(Intune): {paths[1]}')

    # print prime column names for debug
    for col in primeData.columns:
        print(col)

    # filter out colons from MAC addresses in prime data
    primeData['MAC Address'] = primeData['MAC Address'].str.replace(':', '')
