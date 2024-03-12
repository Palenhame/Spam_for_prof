def snail(snail_map):
    if snail_map[0]:
        for i in snail_map:
            if len(i) >= 3:
                pass
            else:
                return i

        answer = []
        first_line, other = snail_map[0], *snail_map
        answer.extend(first_line)
        print(other)
        return answer
    return []


print(snail([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]))
