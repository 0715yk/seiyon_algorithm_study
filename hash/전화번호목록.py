# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42577
# 문제 이름 : 전화번호 목록(lv 12)
# 문제 종류 : Hash(해시)

# 풀이 1)
# 생각 :
# 해시를 이용할 생각을 못해서 이중 for문으로 풀어야겠다는 생각에 앞에서부터(phone_book)하나씩 순회하면서(먼저, 길이를 기준으로 오름차 정렬),
# 첫번째 for문에서 선택된 번호와 그 뒤의 번호를 비교하되, 그 뒤번호의 [0:첫번째 for문에서 선택된 번호의 길이] 만큼만 비교하도록 한다.
# 이런식으로 계속 이중for문을 돌리다가 만약 첫번째 for문의 번호와 2depth의 for문의 번호의 '[0:첫번째 for문에서 선택된 번호의 길이]' 이 부분이 같을 때,
# 바로 False를 리턴해서 함수를 종료하고,
# 그렇지 않은 경우에는 계속 진행하여 for 문이 끝나면 결국 True를 리턴한다

# 풀이 :

def solution1 (phone_book):
    phone_book.sort(key=len)
    logest_len = phone_book[-1]

    for i, number_prev in enumerate(phone_book):
        if i == len(phone_book)-1:
            return True
        for number_next in phone_book[i+1:]:
            if len(number_prev) == logest_len:
                return True
            if number_next[:len(number_prev)] == number_prev:
                return False

    return True

# 결과 :
# 정확성: 83.3
# 효율성: 8.3
# 합계: 91.7 / 100.0

# 분석 : 이중 for문에 phone_book의 길이가 많을수록 두번째 for문 순회 수가 많아져서 효율성에서 불합격을 한 것 같다..

# 해답 풀이 2)
# 생각 : 여기서 어떠게 해시 개념을 이용할지 몰랐는데, 해시를 해시값, 해시함수 등의 개념에 국한되지 않고,
# 자료를 저장할 때 하나의 값에 하나의 인덱스가 있으므로, 탐색 시간이 O(1)이 걸리는 자료구조라는 발상으로 접근해보면,
# 즉, 배열이 아닌 dictionary를 만들어놓고, 순회하면서 한번에 조회를 할 수 있게 만들면 배열의 길이에 국한되지 않고, 효율적인 코드를 짤 수 있을 것.

# 풀이 :
def solution2(phone_book):
    answer = True
    hash_map = {}

    for phone_number in phone_book:
        hash_map[phone_number] = 0
    # 먼저, 주어진 자료를 hash_map으로 생성, 0은 의미없는 디폴트값
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            # 2 depth에서 각각의 번호를 가지고 한번더 순회를 함(번호 하나하나를)
            # 순회를 하면서 앞서 만들어둔 hash_map에 해당 번호가 있으면, 즉, 포함여부를 확인해서 있으면 (이 때, 자기와 같은 것은 무조건 있을테니 제외) ** 이 때, 시간 복잡도 O(1)
            # 접두사 번호가 있는 것이므로 바로 False를 리턴
            # 그렇지 않으면 계속해서 진행
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    # 마지막까지 False 리턴이 안되면 본래 있던 디폴트 값인 answer = True를 리턴
    return answer

# 재고 :
# 이 풀이는 조건에
# phone_book의 길이는 1 이상 1,000,000 이하입니다.
# 각 전화번호의 길이는 1 이상 20 이하입니다.
# 위와 같은 조건이 있기에 효율성을 통과하는 풀이라고 할 수 있다.
# 어찌됐든 이 풀이도 2중 for문을 쓰기 때문에 만약 전화번호의 길이가 1,000,000이라면 비효율적인 코드가 된다.
# 어쨌든, 위의 풀이는 phone_book의 길이가 1,000,000에 가까운 케이스에서
# 2중 for문의 2depth 시행 회수가 글자 길이에 따라 좌우되고, 같은 것이 있는지 탐색을 할 때에는 dictionary에서 찾기 때문에
# O(n)의 탐색이 아닌 O(1)의 탐색이 되어 좀 더 효율적인 코드라고 할 수 있다.
