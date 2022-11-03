function solution(n, left, right) {
  let answer = [];

  for (let i = left; i < right + 1; i += 1) {
    const y = parseInt(i / n);
    const x = i % n;

    answer.push(y >= x ? y + 1 : x + 1);
  }

  return answer;
}
