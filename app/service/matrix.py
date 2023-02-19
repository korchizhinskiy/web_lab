def get_matrix(matrix_size: int = 5) -> None | list[list[int]]:
    """
    Get table of matrix in HTML view.
    """
    rows_list = []
    
    row_numbers = list(range(1, matrix_size+1))
    rows_list.append(row_numbers[:])
    
    if matrix_size < 1:
        return None
    elif matrix_size == 1:
        return rows_list
    else:
        for number in range(2, matrix_size+1):
            row_numbers.insert(0, number)

            row = row_numbers[:matrix_size]
            rows_list.append(row)
    return rows_list
        

