function solution(n, works) {
  const sum = works.reduce((a, c) => a + c, 0);
  if (sum < n) return 0;

  works.sort((a, b) => b - a);

  while (n > 0) {
    const max = works[0];
    for (let i = 0; i < works.length; i += 1) {
      if (works[i] !== max || n === 0) break;

      works[i] -= 1;
      n -= 1;
    }
  }

  return works.reduce((a, c) => a + Math.pow(c, 2), 0);
}
