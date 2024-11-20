def checkmate(board):
    def check_Square():
        lines_board = board.count('\n') + 1  # หาจำนวนบรรทัด
        line1 = board.split('\n')  # แยกบรรทัด
        naltang = len(line1[0])  # หาความยาว line 1
        check = True

        for line_check in line1:
            if len(line_check) != naltang:
                check = False
                break

        if not check:
            print("Error : talang mai pan jatturat")

    def check_King():
        count_K = board.count('K')
        if count_K > 1:
            print("King mak kar 1")
        elif count_K == 0:
            print("mai me King ")

    check_Square()
    check_King()

    allowed_characters = {'.', 'K', 'Q', 'P', 'R'}
    invalid_characters = set(board) - allowed_characters

    if invalid_characters:
        print(f"no: {invalid_characters}")
    else:
        print("no")
