def pattern_d(n):
    big_lst = []
    b_counter = 0

    for i in range(1,n+1):
        counter = 0
        r_num = round(((4 * n) - 3) / 2)
        p_lst = [None] * ((4 * n) - 3)

        if i == 0:
            p_lst[r_num] = items[0]
        else:
            for j in range(r_num, r_num+2*i, 2):
                p_lst[j] = items[(b_counter-counter) % 3]
                counter += 1
            counter = 0
            for k in range(r_num, r_num-2*i, -2):
                p_lst[k] = items[(b_counter-counter) % 3]
                counter += 1

        for l in range(((4 * n) - 3)):
            if p_lst[l] is None:
                p_lst[l] = "-"

        b_counter += 1
        p = "".join(p_lst)
        big_lst.append(p)
    largest = 0
    for i in range(len(big_lst)-2, -1, -1):
        if len(big_lst[i]) > largest:
            largest = len(big_lst[i])
        big_lst.append(big_lst[i])


    return "\n".join(big_lst)
