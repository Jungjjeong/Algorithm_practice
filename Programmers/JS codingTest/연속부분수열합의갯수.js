function solution(elements) {
  let answer = [];
  const elementsArr = [...elements, ...elements];

  for (let i = 1; i <= elements.length; i += 1) {
    for (let j = 0; j < elements.length; j += 1) {
      let sum = 0;

      for (let num = j; num < j + i; num += 1) {
        sum += elementsArr[num];
      }

      answer.push(sum);
    }
  }

  return new Set(answer).size;
}
