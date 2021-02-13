"""출처: 이것이 코딩 테스트다 with 파이썬 (나동빈 지음, 한빛미디어 출판)"""

def rotate_a_matrix_by_90degree(a):
    row_length = len(a)
    column_length = len(a[0])

    res = [[0] * row_length for _ in range(column_length)]
    for r in range(row_length):
        for c in range(column_length):
            res[c][row_length - 1 - r] = a[r][c]
    return res
