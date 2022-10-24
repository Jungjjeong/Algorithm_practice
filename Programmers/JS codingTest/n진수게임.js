function solution(n, t, m, p) {
  let temp = [];
  let totalIdx = 0;

  for (let i = 0; i < t * m; i += 1) {
    const changeNum = i.toString(n).split('');
    changeNum.forEach(
      (num, idx) => (idx + totalIdx) % m === p - 1 && temp.push(num)
    );

    if (temp.length >= t) break;
    totalIdx += changeNum.length;
  }

  return temp
    .slice(0, t)
    .map((t) => t.toUpperCase())
    .join('');
}
