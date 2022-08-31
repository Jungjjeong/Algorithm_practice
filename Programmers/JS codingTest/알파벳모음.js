function solution(word) {
  let answer = 0;
  // A, E => A(1), AA(2), AE(3), E(4), EA(5), EE(6) (6가지)
  // AA -> AE => 1
  // A -> E는 ? => 2(자릿수) + 1

  // A, E, I => A, AA, AAA, AAE, AAI, AE, AEA, AEE, AEI, AI, AIA, AIE, AII, E, EA, EAA ... (39)
  // AAA -> AAE => +1
  // AA -> AE => 3(자릿수) + 1
  // A -> E => 3 * (3 + 1) + 1 = 13
  // EAA는 몇번째? A -> E = 1 + 13 / A는 그대로 1 / A는 그대로 1 => 16번째
  // AIA는 몇번째? A는 그대로 1 / AA -> AI = 1 + 4 + 4 / A는 그대로 1 => 10번째
  let alphabet = ['A', 'E', 'I', 'O', 'U'];
  let nextWord = [781, 156, 31, 6, 1]; // 자릿수 * 5제곱

  word.split('').forEach((w, i) => {
    answer += 1 + alphabet.indexOf(w) * nextWord[i];
  });

  return answer;
}
