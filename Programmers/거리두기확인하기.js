function bfs(y, x, placeArr) {
  const dx = [0, 0, 0, 0, 1, 2, -1, -2, 1, 1, -1, -1];
  const dy = [1, 2, -1, -2, 0, 0, 0, 0, 1, -1, -1, 1];
  console.log(y, x);

  for (let i = 0; i < 12; i += 1) {
    const ny = y + dy[i];
    const nx = x + dx[i];

    if (ny < 0 || ny >= 5 || nx < 0 || nx >= 5) {
      continue;
    } else if (placeArr[ny][nx] === 'P') {
      console.log('P입니다');
      if (i === 1) {
        if (placeArr[ny - 1][nx] !== 'X') {
          console.log(1);
          return false;
        }
      } else if (i === 3) {
        if (placeArr[ny + 1][nx] !== 'X') {
          console.log(3);
          return false;
        }
      } else if (i === 5) {
        if (placeArr[ny][nx - 1] !== 'X') {
          console.log(5);
          return false;
        }
      } else if (i === 7) {
        if (placeArr[ny][nx + 1] !== 'X') {
          console.log(7);
          return false;
        }
      } else if (i === 8) {
        if (placeArr[ny - 1][nx] !== 'X' || placeArr[ny][nx - 1] !== 'X') {
          console.log(8);
          return false;
        }
      } else if (i === 9) {
        if (placeArr[ny + 1][nx] !== 'X' || placeArr[ny][nx - 1] !== 'X') {
          console.log(9);
          return false;
        }
      } else if (i === 10) {
        if (placeArr[ny + 1][nx] !== 'X' || placeArr[ny][nx + 1] !== 'X') {
          console.log(10);
          return false;
        }
      } else if (i === 11) {
        if (placeArr[ny - 1][nx] !== 'X' || placeArr[ny][nx + 1] !== 'X') {
          console.log(11);
          return false;
        }
      } else {
        console.log('ny nx', ny, nx);
        return false;
      }
    }
  }

  return true;
}

function solution(places) {
  let answer = [1, 1, 1, 1, 1];

  places.forEach((placeArr, index) => {
    console.log('---', placeArr);
    placeArr.forEach((place, i) => {
      place.split('').forEach((p, j) => {
        if (p === 'P') {
          const bfsResult = bfs(i, j, placeArr);
          console.log(bfsResult);
          if (bfsResult === false) {
            console.log('0으로!@');
            answer[index] = 0;
            console.log(answer);
            return;
          }
        }
      });
    });
  });

  return answer;
}

console.log(
  solution([
    ['POOOP', 'OXXOX', 'OPXPX', 'OOXOX', 'POXXP'],
    ['POOPX', 'OXPXP', 'PXXXO', 'OXXXO', 'OOOPP'],
    ['PXOPX', 'OXOXP', 'OXPOX', 'OXXOP', 'PXPOX'],
    ['OOOXX', 'XOOOX', 'OOOXX', 'OXOOX', 'OOOOO'],
    ['PXPXP', 'XPXPX', 'PXPXP', 'XPXPX', 'PXPXP'],
  ])
);
