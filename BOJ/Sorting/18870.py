# BOJ 18870 μ’νμμΆ
def solution():
    n = int(input())
    coordinates = list(map(int, input().split()))
    sorted_coordinates = sorted(set(coordinates))
    coordinate_dictionary = {}
    for i, v in enumerate(sorted_coordinates):
        coordinate_dictionary[v] = i
    answer = []
    for c in coordinates:
        answer.append(coordinate_dictionary[c])

    print(" ".join(str(i) for i in answer))


if '__main__' == __name__:
    solution()
    