let animal = ['척추동물', '어류', '척추동물', '무척추동물', '파충류', '척추동물', '어류', '파충류'];

function solution(animal, 자리수){
    let chair = [];
    let answer = 0;

    // shift() 맨 앞 요소 [0]선택
    for(const 개별동물 of animal){
        if(chair.length < 3){
            if (chair.includes(개별동물)){ // hit
                chair.splice(chair.indexOf(개별동물), 1)
                chair.push(개별동물); 
                answer += 1; // 1초
            } else { // Not hit
                chair.push(개별동물); // -> 앞에 넣음
                answer += 60; // 1분
            }
        } else {
            if (chair.includes(개별동물)){ // hit
                chair.splice(chair.indexOf(개별동물), 1)
                chair.push(개별동물);
                answer += 1; // 1초
            } else{ // Not hit
                chair.shift()
                chair.push(개별동물); // -> 앞에 넣음
                answer += 60; // 1분
            }
        }
        console.log(chair);
    }
    console.log(parseInt(answer/60, 10),"분",answer%60,"초");
    return answer
}

solution(animal,3);