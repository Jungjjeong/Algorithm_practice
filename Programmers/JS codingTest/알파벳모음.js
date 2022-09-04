function solution(word) {
  let answer = 0;
  const alphabet = ['A', 'E', 'I', 'O', 'U'];
  const nextWord = [781, 156, 31, 6, 1]; // 자릿수 * 5제곱

  word.split('').forEach((w, i) => {
    answer += 1 + alphabet.indexOf(w) * nextWord[i];
  });

  return answer;
}
