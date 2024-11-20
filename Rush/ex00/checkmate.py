def checkmate(board):

    lines_board = board.count('\n') + 1  # หาจำนวนบรรทัด

    line1 = board.split('\n') # แยกบรรทัด

    naltang = len(line1[0]) # หาความยาว line 1
    check = True

    for line_check in line1:
        if len(line_check) != naltang:
            check = False
            break

    if check == False :
        print("Eror the talang is not jatturat")
