function checkStr(str) {
  const regex = /[a-zA-Z]{2}/;
  let result = [];

  for (let i = 0; i < str.length - 1; i++) {
    const sliceStr = str.slice(i, i + 2);
    if (regex.test(sliceStr)) result.push(sliceStr.toLowerCase());
  }

  return result;
}

function solution(str1, str2) {
  const veriStr1 = checkStr(str1);
  const veriStr2 = checkStr(str2);
  const union = new Set([...veriStr1, ...veriStr2]);

  let intersectionLen = 0;
  let unionLen = 0;

  for (const slice of union) {
    const count1 = veriStr1.filter((x) => x === slice).length;
    const count2 = veriStr2.filter((x) => x === slice).length;

    intersectionLen += Math.min(count1, count2);
    unionLen += Math.max(count1, count2);
  }

  return unionLen === 0
    ? 65536
    : Math.floor((intersectionLen / unionLen) * 65536);
}
