# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42576
# 문제 이름 : 완주하지 못한 선수(lv 1)
# 문제 종류 : Hash(해시)

# 풀이 1)
def solution1(participant, completion):
    # 생각 :
    # participant와 completion은 무조건 길이가 1이 차이남(문제 조건)
    # 따라서 하나 더 긴 participant list에서 completion을 빼면 완주하지 못한 즉, 둘의 '차이점'인 값을 얻을 수 있음
    # 따라서, 둘을 빼는 방법을 고민

    # 풀이 :
    # 1) 먼저 둘의 순서를 같게 한다.
    participant.sort()
    completion.sort()
    # 2) 그 다음 완주자 명단을 순회하면서 1:1 매칭을 해본다.
    for idx, name in enumerate(completion):
        if participant[idx] != completion[idx]:
            return participant[idx]
        # 이 때, 순서가 같은 두 list에서 같은 index에 다른 값이 나오면 반드시 그 값이 둘의 차이가 되는 값이므로 바로 리턴
    # 순회를 다 했음에도 리턴이 되지 않으면 결국 participant의 마지막 값이 차이가 되는 값이므로 마지막 값을 리턴
    return participant[len(participant)-1]

# 인터넷 검색을 참고, 그리고 python에 내장돼있는 hash()를 이용한 풀이
# 풀이 2)
def solution2(participant, completion):
    # 생각 :
    # 해쉬에서 해쉬 함수에 key를 넣으면 반드시 같은 해시값이 나오는 것을 이용해볼 수 없을까?
    # 예를 들어, 이 문제를 예로 들면, hash('mislev') 를 하 반드시 8722199181897696111가 나온다.
    # 이 성질을 이용해서 문제를 풀어보면,
    # participant을 순회하면서 명단 속 이름들의 해시값을 더하면서 dictionary에 해쉬(키), 이름(값)으로 저장을 하며 순회한다.
    # 이 후, completion에서 이전에 participant의 모든 해시값을 더한 변수 hash_sum에서 다시 completion 명단의 해시값을 빼면서 순회한다.
    # 그러면 결국 hash_sum에 남아있는 해시값이 participant 중 완주히지 못한, 즉, completion에는 없는 이름의 해시값일 것이기에
    # 마지막에 위에서 만들어놓은 dictionary에 해당 해시값을 참조하면 값이 나오고, 해당 값이 완주하지 못한 선수가 된다.

    # 풀이 :
    # 1) participant를 for문으로 순회하면서 hash_sum에 해시값을 더하면서 동시에 hash_table이라는 dict형 자료에 해시값을 키로, 이름을 값으로 저장한다.
    hash_sum = 0
    hash_table = {}

    for name in participant:
        hash_table[hash(name)] = name
        hash_sum += hash(name)
    # 2) 현재 hash_sum에는 participant 리스트의 이름들의 해시값이 모두 더해진 상태이고, hash_table에는 해시값(키), 이름(값)인 딕셔너리가 들어있다
    # 3) 그러면 마지막으로 completion을 for문으로 순회하면서 이번에는 hash_sum에서 completion 내의 이름의 해시값을 하나하나 빼주면서 순회한다
    for name in completion:
        hash_sum -= hash(name)

    return hash_table[hash_sum]