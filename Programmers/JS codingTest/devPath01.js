function solution(bricks) {
  const answer = [];
  const maxWidth = bricks.reduce((a, c) => a + c, 0);

  for (let i = maxWidth; i >= Math.max(...bricks); i -= 1) {
    let heightResult = 0;
    let tempHeight = 0;

    for (let bIdx = 0; bIdx < bricks.length; bIdx += 1) {
      tempHeight += bricks[bIdx];

      if (tempHeight === i) {
        heightResult += 1;
        tempHeight = 0;
      } else if (tempHeight > i) break;
    }

    if (heightResult !== 0 && tempHeight === 0) answer.push(heightResult);
  }

  return answer
    .filter((element, index) => answer.indexOf(element) === index)
    .sort((a, b) => a - b);
}
