function checkWord(prevWord, nextWord) {
  let notMatchNum = 0;
  const prevArr = prevWord.split('');
  const nextArr = nextWord.split('');

  for (let i = 0; i < prevWord.length; i += 1) {
    if (prevArr[i] !== nextArr[i]) notMatchNum += 1;
  }

  return notMatchNum === 1 ? true : false;
}

function solution(begin, target, words) {
  let answer = 51;
  let visit = new Array(words.length).fill(0);

  function dfs(word, count) {
    if (word === target) {
      if (count < answer) answer = count;
      return;
    }

    for (let i = 0; i < words.length; i += 1) {
      const nextWord = words[i];
      if (visit[i] === 1 || !checkWord(word, nextWord)) continue;

      visit[i] = 1;
      dfs(nextWord, count + 1);
      visit[i] = 0;
    }
  }

  dfs(begin, 0);
  return answer === 51 ? 0 : answer;
}
