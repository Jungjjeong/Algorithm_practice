function solution(S, pattern) {
  let answer = 0;
  const sortPattern = pattern
    .split('')
    .sort((a, b) => (a > b ? 1 : -1))
    .join('');
  const splitSArr = S.split('');

  for (let i = 0; i < S.length - pattern.length + 1; i += 1) {
    const sliceS = splitSArr
      .slice(i, i + pattern.length)
      .sort((a, b) => (a > b ? 1 : -1))
      .join('');

    if (sliceS === sortPattern) answer += 1;
  }

  return answer;
}
