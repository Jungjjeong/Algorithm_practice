function solution(numbers, target) {
  let answer = 0;

  function dfs(sumNums, count) {
    if (count === numbers.length) {
      if (sumNums === target) answer += 1;
      return;
    }

    for (let i = 0; i < 2; i += 1) {
      const number = numbers[count];
      if (i === 0) dfs(sumNums + number, count + 1);
      else if (i === 1) dfs(sumNums - number, count + 1);
    }
  }

  dfs(0, 0);

  return answer;
}
