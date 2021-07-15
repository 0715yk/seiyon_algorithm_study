function solution(n, vertex) {
  let answer = 0;
  const nodes = new Array(n + 1);
  for (let i = 0; i < n + 1; i++) {
    nodes[i] = new Array();
  }

  for (let [start, end] of vertex) {
    nodes[start].push(end);
    nodes[end].push(start);
  }

  function bfs() {
    const Q = [];
    const visit = new Map();
    let v;
    let num;
    let QLen = 1;

    Q.push(1);
    visit.set(1, 1);

    while (Q.length !== 0) {
      QLen = Q.length;
      num = Q.length;
      while (QLen !== 0) {
        QLen -= 1;
        v = Q.shift();

        for (let nextNode of nodes[v]) {
          if (visit.get(nextNode) !== 1) {
            Q.push(nextNode);
            visit.set(nextNode, 1);
          }
        }
      }
    }
    return num;
  }

  answer = bfs();

  return answer;
}
