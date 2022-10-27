function solution(dirs) {
  let answer = 0;
  let coord = { x: 0, y: 0 };
  let visit = [];

  dirs.split('').forEach((dir) => {
    const [x, y] = [coord.x, coord.y];

    if (dir === 'U') {
      if (y === 5) return;

      const [dir1, dir2] = [`${x}${y}${x}${y + 1}`, `${x}${y + 1}${x}${y}`];

      if (visit.indexOf(dir1) === -1 && visit.indexOf(dir2) === -1) answer += 1;
      visit.push(dir1);
      coord.y += 1;
    } else if (dir === 'L') {
      if (x === -5) return;

      const [dir1, dir2] = [`${x}${y}${x - 1}${y}`, `${x - 1}${y}${x}${y}`];

      if (visit.indexOf(dir1) === -1 && visit.indexOf(dir2) === -1) answer += 1;
      visit.push(dir1);
      coord.x -= 1;
    } else if (dir === 'R') {
      if (x === 5) return;

      const [dir1, dir2] = [`${x}${y}${x + 1}${y}`, `${x + 1}${y}${x}${y}`];

      if (visit.indexOf(dir1) === -1 && visit.indexOf(dir2) === -1) answer += 1;
      visit.push(dir1);
      coord.x += 1;
    } else if (dir === 'D') {
      if (y === -5) return;

      const [dir1, dir2] = [`${x}${y}${x}${y - 1}`, `${x}${y - 1}${x}${y}`];

      if (visit.indexOf(dir1) === -1 && visit.indexOf(dir2) === -1) answer += 1;
      visit.push(dir1);
      coord.y -= 1;
    }
  });

  console.log(coord);
  return answer;
}
