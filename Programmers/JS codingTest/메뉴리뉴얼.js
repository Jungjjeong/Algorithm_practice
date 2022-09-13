function combination(arr, num) {
  const res = [];
  if (num === 1) return arr.map((v) => [v]);

  arr.forEach((v, idx, arr) => {
    const rest = arr.slice(idx + 1);
    const combinations = combination(rest, num - 1);
    const attach = combinations.map((combination) => [v, ...combination]);

    res.push(...attach);
  });

  return res;
}

function solution(orders, course) {
  let answer = [];
  let orderObject = {};
  let combiRes = [];

  orders.forEach((courseOrder) => {
    const courseOrderLen = courseOrder.length;

    course.forEach((c) => {
      if (courseOrderLen < c) return false;

      const combiArr = combination(courseOrder.split(''), c);
      combiRes = [...combiRes, ...combiArr];
    });
  });

  combiRes.forEach((res) => {
    const resStr = res.sort().join('');
    if (orderObject.hasOwnProperty(resStr)) orderObject[resStr] += 1;
    else orderObject[resStr] = 1;
  });

  const sortObject = Object.fromEntries(
    Object.entries(orderObject).sort(([, a], [, b]) => b - a)
  );
  let answerObject = {};

  for (let orderName in sortObject) {
    const orderValue = sortObject[orderName];
    const orderLength = orderName.length;

    if (orderValue < 2) continue;

    if (orderLength in answerObject === false) {
      answerObject[orderLength] = orderValue;
      answer.push(orderName);
    } else if (answerObject[orderLength] === orderValue) {
      answer.push(orderName);
    }
  }

  return answer.sort();
}
