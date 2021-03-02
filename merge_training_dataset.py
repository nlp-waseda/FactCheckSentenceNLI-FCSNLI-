import argparse

import pandas as pd

"""
複数のNLIの訓練データを結合するプログラム
"""

INDEX_NUM = -1


def edit_index(index: int) -> int:
    global INDEX_NUM
    INDEX_NUM += 1
    return INDEX_NUM


def main():
    parser = argparse.ArgumentParser(
        prog='merge_training_dataset.py',
        usage='複数の訓練データを結合するプログラム',
        description='使い方説明',
        epilog='end',
        add_help=True
    )

    parser.add_argument('training_files', nargs='*', help='訓練データ（半角スペースで複数ファイル選択可能）')
    args = parser.parse_args()

    print('-------------------------------')
    for file in args.training_files:
        print(file)
    print('-------------------------------')

    df_list = \
        list(map(
            lambda training_file: pd.read_csv(training_file, sep='\t'),
            args.training_files))
    new_df = pd.concat(df_list)
    new_df['index'] = new_df['index'].map(edit_index)

    # 出力するファイル名
    new_df.to_csv('output_file_name.tsv', sep='\t', index=False)


if __name__ == '__main__':
    main()
