function solution(k, dungeons) {
  let answer = -1;
  let visit = new Array(dungeons.length).fill(0);

  function dfs(curK, count) {
    if (answer < count) answer = count;
    if (count === dungeons.length) return;

    for (let i = 0; i < dungeons.length; i += 1) {
      const [minK, minusK] = dungeons[i];

      if (visit[i] === 1 || minK > curK) continue;

      visit[i] = 1;
      dfs(curK - minusK, count + 1);
      visit[i] = 0;
    }
  }

  for (let i = 0; i < dungeons.length; i += 1) {
    if (k < dungeons[i][0]) continue;

    visit[i] = 1;
    dfs(k - dungeons[i][1], 1);
    visit[i] = 0;
  }

  return answer;
}
