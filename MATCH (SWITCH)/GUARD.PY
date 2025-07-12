month=5
day=4
match day:
    case 1| 2|3|4|5 if month == 4:

        print("A WEELKEND IN April")
    case 1|2|3|4|5 if month == 5:
        print("A weekend in May")
    case _:
        print("NO MATCH")    