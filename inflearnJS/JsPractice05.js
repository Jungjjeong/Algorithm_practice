let graph = {100: new Set([67, 66]),
    67: new Set([100, 82, 63]),
    66: new Set([100, 73, 69]),
    82: new Set([67, 61, 79]),
    63: new Set([67]),
    73: new Set([66]),
    69: new Set([66, 65, 81]),
    61: new Set([82]),
    79: new Set([82, 87, 77]),
    65: new Set([69, 84, 99]),
    81: new Set([69]),
    87: new Set([79, 31, 78]),
    77: new Set([79]),
    84: new Set([65]),
    99: new Set([65]),
    31: new Set([87]),
    78: new Set([87])};

function 깊이우선탐색Max(graph, start){
    let 방문 = [];
    let stack = [start];

    while(stack){
        let n = 0; // 다음 방문 노드
        n = stack.pop(); // 마지막 요소 꺼냄
        if(!방문.includes(n)) {
            방문.push(n);
            let 차집합 = new Set([...graph[n]].filter(x => !(new Set(방문).has(x))));
            if([...차집합].length == 0){ // 집합은 length가 항상 0이므로 꼭 list화 시키자 
                break
            }
            stack.push(Math.max(...차집합));
            // console.log('방문 :',방문);
            // console.log('stack :',stack);
        }
        if (stack.length == 0){
            break;
        }
    }
    return 방문;
}

function 깊이우선탐색Min(graph, start){
    let 방문 = [];
    let stack = [start];

    while(stack){
        let n = 0; // 다음 방문 노드
        n = stack.pop(); // 마지막 요소 꺼냄
        if(!방문.includes(n)) {
            방문.push(n);
            let 차집합 = new Set([...graph[n]].filter(x => !(new Set(방문).has(x))));
            if([...차집합].length == 0){ // 집합은 length가 항상 0이므로 꼭 list화 시키자 
                break
            }
            stack.push(Math.min(...차집합));
            // console.log('방문 :',방문);
            // console.log('stack :',stack);
        }
        if (stack.length == 0){
            break;
        }
    }
    return 방문;
}
 // ...은 list 형태를 숫자 나열로 풀어주는 역할
 // filter 특정 조건 만족하는 값들만 출력
 // map 은 특정 값을 원하는 대로 변환하여 반환


console.log(깊이우선탐색Max(graph, 100));
maxResult = 깊이우선탐색Max(graph, 100);
console.log(깊이우선탐색Min(graph, 100));
minResult = 깊이우선탐색Min(graph, 100);
let aresult = ''
for(var v of maxResult){
    aresult += String.fromCharCode(v);
}
let iresult = ''
for(var v of minResult){
    iresult += String.fromCharCode(v);
}
console.log(aresult);
console.log(iresult);