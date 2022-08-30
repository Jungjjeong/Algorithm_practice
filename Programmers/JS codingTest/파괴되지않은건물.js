function solution(board, skill) {
  let answer = 0;
  const row = board.length;
  const col = board[0].length;
  let imosArr = Array.from({ length: row + 1 }, () =>
    new Array(col + 1).fill(0)
  );

  for (const s of skill) {
    const [type, r1, c1, r2, c2, degree] = s;

    imosArr[r1][c1] += type === 1 ? -degree : degree;
    imosArr[r1][c2 + 1] += type === 1 ? degree : -degree;
    imosArr[r2 + 1][c1] += type === 1 ? degree : -degree;
    imosArr[r2 + 1][c2 + 1] += type === 1 ? -degree : degree;
  }

  for (let i = 0; i < row; i += 1) {
    let sum = 0;
    for (let j = 0; j < col; j += 1) {
      sum += imosArr[i][j];
      imosArr[i][j] = sum;
    }
  }

  for (let i = 0; i < col; i += 1) {
    let sum = 0;
    for (let j = 0; j < row; j += 1) {
      sum += imosArr[j][i];
      imosArr[j][i] = sum;
    }
  }

  for (let i = 0; i < row; i += 1) {
    for (let j = 0; j < col; j += 1) {
      board[i][j] += imosArr[i][j];

      if (board[i][j] > 0) {
        answer++;
      }
    }
  }

  return answer;
}
