function solution(msg) {
  let dict = [
    '',
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z',
  ];
  const msgArr = msg.split('');
  let answer = [];
  let prevStr = '';

  while (msgArr.length > 0) {
    const curChar = msgArr[0];
    const curStr = prevStr + curChar;
    const dictIdx = dict.indexOf(curStr);

    if (dictIdx !== -1) {
      prevStr = curStr;
      msgArr.shift();
    } else {
      answer.push(dict.indexOf(prevStr));
      dict.push(curStr);
      prevStr = '';
    }
  }

  const idx = dict.indexOf(prevStr);
  idx === -1 ? answer.push(dict.length) : answer.push(idx);

  return answer;
}
