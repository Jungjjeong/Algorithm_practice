function solution(cacheSize, cities) {
  let answer = 0;
  let cache = [];

  if (cacheSize === 0) return 5 * cities.length;

  cities.forEach((city) => {
    const cityLower = city.toLowerCase();
    const cacheIdx = cache.indexOf(cityLower);

    if (cacheIdx !== -1) {
      cache.splice(cacheIdx, 1);
      cache.push(cityLower);
      answer += 1;
    } else {
      if (cache.length >= cacheSize) cache.shift();

      cache.push(cityLower);
      answer += 5;
    }
  });

  return answer;
}
