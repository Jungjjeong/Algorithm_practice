function solution(m, n, board) {
  const deleteBoard = board.map((b) => b.split(''));

  while (true) {
    let deleteArr = [];

    for (let i = 0; i < deleteBoard.length - 1; i += 1) {
      for (let j = 0; j < deleteBoard[0].length - 1; j += 1) {
        if (
          deleteBoard[i][j] &&
          deleteBoard[i][j] === deleteBoard[i + 1][j] &&
          deleteBoard[i][j] === deleteBoard[i][j + 1] &&
          deleteBoard[i][j] === deleteBoard[i + 1][j + 1]
        ) {
          deleteArr.push([i, j]);
        }
      }
    }

    if (deleteArr.length === 0)
      return deleteBoard.reduce(
        (a, cur) => a + cur.filter((c) => c === null).length,
        0
      );

    deleteArr.forEach((idx) => {
      const [x, y] = idx;

      deleteBoard[x][y] = 1;
      deleteBoard[x + 1][y] = 1;
      deleteBoard[x][y + 1] = 1;
      deleteBoard[x + 1][y + 1] = 1;
    });

    for (let j = 0; j < deleteBoard[0].length; j += 1) {
      for (let i = 0; i < deleteBoard.length; i += 1) {
        if (deleteBoard[i][j] === 1) {
          for (let idx = i; idx > 0; idx -= 1) {
            if (deleteBoard[idx - 1][j])
              deleteBoard[idx][j] = deleteBoard[idx - 1][j];
            else deleteBoard[idx][j] = null;
          }

          deleteBoard[0][j] = null;
        }
      }
    }
  }
}
