


#출력 함수
def print_result(visited, distance):
    print("총", len(visited), "개의 노드를 방문하였습니다.")
    print("방문한 노드는", visited, "입니다.")
    print("최단거리는", distance, "입니다.")

#main
if __name__ == "__main__":
    visited = "3개"
    distance = 20

    print_result(visited, distance)
