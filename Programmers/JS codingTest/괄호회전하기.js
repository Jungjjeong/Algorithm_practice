function checkBracket(bracketArr) {
  const bracketObj = { '[': ']', '{': '}', '(': ')' };
  const stack = [];

  if (bracketArr[0] == ']' || bracketArr[0] == '}' || bracketArr[0] == ')')
    return false;

  for (let i = 0; i < bracketArr.length; i += 1) {
    if (bracketArr[i] in bracketObj) {
      stack.push(bracketArr[i]);
      continue;
    }

    const popBracket = stack.pop();
    if (bracketObj[popBracket] !== bracketArr[i]) return false;
  }

  return stack.length === 0 ? true : false;
}

function solution(s) {
  var answer = 0;
  let splitS = s.split('');

  if (s.length === 1) return 0;

  for (let i = 0; i < splitS.length; i += 1) {
    const popS = splitS.pop();
    splitS.unshift(popS);

    if (checkBracket(splitS)) answer += 1;
  }

  return answer;
}
