function toRemoveZero(str) {
  const strArr = str.split('');
  const removeZero = strArr.filter((s) => s === '0').length;
  const changeStrArr = strArr.filter((s) => s !== '0');

  return [changeStrArr, removeZero];
}

function solution(s) {
  let answer = [0, 0];
  let binary = s;

  while (true) {
    if (binary === '1') break;

    const [changeStrArr, count] = toRemoveZero(binary);
    const binaryStr = changeStrArr.length.toString(2);
    binary = binaryStr;
    answer[1] += count;
    answer[0] += 1;
  }

  return answer;
}
