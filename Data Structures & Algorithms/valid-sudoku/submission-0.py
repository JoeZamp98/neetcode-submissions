class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        all_squares = [[] for x in range(9)]
        all_columns = [[] for x in range(9)]

        for r, row in enumerate(board):

            # build columns
            for c, val in enumerate(row):

                all_columns[c].append(val)

            # build squares
            sq_a, sq_b, sq_c = row[0:3], row[3:6], row[6:9]

            if r in [0, 1, 2]:
                
                all_squares[0].extend(sq_a)
                all_squares[1].extend(sq_b)
                all_squares[2].extend(sq_c)

            elif r in [3, 4, 5]:

                all_squares[3].extend(sq_a)
                all_squares[4].extend(sq_b)
                all_squares[5].extend(sq_c)

            elif r in [6, 7, 8]:

                all_squares[6].extend(sq_a)
                all_squares[7].extend(sq_b)
                all_squares[8].extend(sq_c)

        print(all_squares)

        for group_type in [board, all_squares, all_columns]:

            for unit in group_type:

                if len(unit) == 9:

                    unit_digits = [int(x) for x in unit if x.isdigit()]

                    unique_condition = len(set(unit_digits)) == len(unit_digits)
                    min_condition = min(unit_digits) >= 1 if unit_digits else True
                    max_condition = max(unit_digits) <= 9 if unit_digits else True

                    unit_result = unique_condition & min_condition & max_condition

                    if unit_result == False:

                        return False                

                else: 

                    return False

        return True