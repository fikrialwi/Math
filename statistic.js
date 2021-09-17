const average = function (arr){
  return arr.reduce((a,b) => a+b)/arr.length
}

const count = function (arr){
  return arr.length
}

const median = function (arr){
  arr.sort((a,b) => a-b)
  return count(arr)%2 === 0? (arr[count(arr)/2-1] +  arr[count(arr)/2])/2 : arr[Math.floor(count(arr)/2)]
}


function modus(arr){
	let max =Math.max(...arr)+ 1;
	let count = new Array(max);
	for (let i = 0; i < max; i++)
		count[i] = 0;
	for (let i = 0; i < arr.length; i++)
		count[arr[i]]++;
	let mode = 0;
	let k = count[0];
	for (let i = 1; i < max; i++) {
		if (count[i] > k) {
			k = count[i];
			mode = i;
		}
	}

	return mode
}
