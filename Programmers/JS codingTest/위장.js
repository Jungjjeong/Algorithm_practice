function solution(clothes) {
  let clothesObj = {};
  let answer = 1;

  clothes.forEach((cloth) => {
    const [clothName, clothType] = cloth;
    if (clothType in clothesObj) clothesObj[clothType] += 1;
    else clothesObj[clothType] = 1;
  });

  const objValueArr = Object.values(clothesObj);
  objValueArr.forEach((value) => (answer *= value + 1));

  return answer - 1;
}
