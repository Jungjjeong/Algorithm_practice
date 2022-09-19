function solution(N, fees, dest) {
  let answer = 10000000000000;

  const path = [1];
  const visited = new Array(fees.length).fill(0);

  const dfs = (curBank, count, curFees) => {
    if (curFees > answer) return;
    if (curBank === dest) {
      if (answer > curFees) answer = curFees;
      return true;
    }

    for (let i = 0; i < fees.length; i += 1) {
      if (visited[i] === 1) continue;

      if (fees[i][0] === curBank) {
        visited[i] = 1;
        path.push(fees[i][1]);
        dfs(fees[i][1], count + 1, curFees + fees[i][2]);
        visited[i] = 0;
        path.pop();
      } else if (fees[i][1] === curBank) {
        visited[i] = 1;
        path.push(fees[i][0]);
        dfs(fees[i][0], count + 1, curFees + fees[i][2]);
        visited[i] = 0;
        path.pop();
      }
    }
  };

  dfs(1, 0, 0);

  return answer;
}
