function solution(fees, records) {
	let answer = [];
	let carObj = {}
	
	records.sort((a, b) => a.split(' ')[1] - b.split(' ')[1]).forEach(record => {
			const [time, carNum, history] = record.split(' ');
			const splitTime = time.split(':');
			const minuteTime = parseInt(splitTime[0]) * 60 + parseInt(splitTime[1]);
			
			if (!(carNum in carObj)) carObj[carNum] = [minuteTime];
			else carObj[carNum].push(minuteTime);
	})
	
	for (key in carObj) {
			const value = carObj[key];
			let price = 0;
			
			for (let i=0; i<value.length; i+=2) {
					if (!value[i+1]) price += ((60 * 23) + 59) - value[i];
					else price += value[i+1] - value[i];
			}
			
			const calculatePrice = price < fees[0] ? fees[1] : fees[1] + Math.ceil((price-fees[0]) / fees[2]) * fees[3];  
			answer.push([parseInt(key), calculatePrice]);
	}
	
	return answer.sort((a, b) => a[0] - b[0]).flatMap(v => v[1]);
}