function solution(arr1, arr2) {
  const [row, col] = [arr1.length, arr2[0].length];
  let answer = new Array(row).fill().map((_) => new Array(col).fill(0));

  for (let i = 0; i < row; i += 1) {
    for (let j = 0; j < col; j += 1) {
      answer[i][j] = arr1[i].reduce((a, c, i) => a + c * arr2[i][j], 0);
    }
  }

  return answer;
}
