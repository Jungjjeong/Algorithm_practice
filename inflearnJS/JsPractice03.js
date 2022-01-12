// 9시 부터 21시 = 12시간
// 9시       25
// 9시 10분  40
// 9시 20분  55
// 9시 30분  70
// 9시 40분  85
// 9시 50분  100 => 한시간에 총 100명 탑승

// 하루동안 1200명 탑승

let 대기인원 = 1200202;
// 우리는 대기인원 다음과 다음에 탑승
// 서로 다른 배를 타야할 경우, 뒷 배를 탑승한다.

// 현재 날짜는 2020년 1월 1일

// 1 ~ 10월, 2의 10승~ 2의 1승
let 일수 = parseInt(대기인원/1200);
console.log(일수);

let 일년일수 = 0;
for(var i = 1; i<11; i++){
    일년일수 += 2**i;
}

let 남은일수 = 일수 % 일년일수;
let month = 0;
for(var i = 10; i>0; i--){
    month += 1;
    if(남은일수 < 2**i){
        console.log(month)
        console.log(남은일수)
        break;
    }
    남은일수 -= 2**i;
}

let year = parseInt(일수 / 일년일수) + 2020;
대기인원 -= 일년일수 * (year-2020) * 1200;
console.log(대기인원)


console.log("year :",year)
console.log("남은일수 :",남은일수)

let 시간당태움 = 대기인원 % 1200;
let 시 = 9;
for(var i = 0; i<12; i++){
    if(시간당태움 < 100){
        console.log(시간당태움);
        console.log(시 + i);
        시 += i;
        break;
    }
    시간당태움 -= 100;
}

let 분인원 = 25;
let 분 = 0;
for(var i = 0; i<6; i++){
    if(시간당태움+1 < 분인원){
        console.log(시간당태움);
        console.log(i*10 + 분)
        break;
    }
    시간당태움 -= 분인원;
    분인원 += 15;
}

console.log(year,'년',month,'월',남은일수,'일',시,'시',분,'분','출발')