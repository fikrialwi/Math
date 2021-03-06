const matrix = (e) =>{
  for(let i = 1; i < e.length;i++){
    if(e[0].length !== e[i].length){
      return "Your matrix can't execute because your array not complet"
    }
  }
  return e
} 
const size = (el) =>{
  return [el.length, el[0].length]
}
const zero = function (a,b = a){
  let col = []
  for(let i = 0; i < a; i++){
    let row = []
    for(let j = 0; j < b; j++){
      row.push(0)
    }
    col.push(row)
  }
  return col
}
const sameMatrix = function (n,a,b = a){
  let col = []
  for(let i = 0; i < a; i++){
    let row = []
    for(let j = 0; j < b; j++){
      row.push(n)
    }
    col.push(row)
  }
  return col
}
const identity = function (a,b = a) {
  let result = zero(a,b);
  for(let i = 0;i < a; i++){
    result[i][i] ++ 
  }
  return result
}
const add = function(a,b) {
  if(size(a)[0] !== size(b)[0] || size(a)[1] !== size(b)[1]){
    return "your matrix should have same size"
  }
  let result = []
  for(let i = 0; i < a.length; i++){
    let res = []
    for(let j = 0; j < a[i].length; j++){
      res.push(a[i][j]+b[i][j])
    }
    result.push(res)
  }
  return result
}
const subtrac = function(a,b) {
  if(size(a)[0] !== size(b)[0] || size(a)[1] !== size(b)[1]){
    return "your matrix should have same size"
  }
  let result = []
  for(let i = 0; i < a.length; i++){
    let res = []
    for(let j = 0; j < a[i].length; j++){
      res.push(a[i][j]-b[i][j])
    }
    result.push(res)
  }
  return result
}
const multiply = function (arr1,arr2) {
  if(size(arr1)[1] !== size(arr2)[0]){
    return "You should have matrix 2 matrix A & B that same number of column A and number of row B"
  }
  let result = zero(size(arr1)[0],size(arr2)[1])
  for(let i = 0; i < size(arr1)[0]; i++){
    for(let j = 0; j < size(arr2)[1];j++){
      for(let k = 0; k < size(arr1)[1]; k++){
        result[i][j] = result[i][j] + arr1[i][k]*arr2[k][j]
      }
    }
  }
  return result
}


const scalar = function (arr,s){
  if(!Array.isArray(arr)){
    [arr, s] = [s, arr]
  }
  return arr.map(el => el.map(e => e*s))
}

const transpose = (arr) => {
  let res = zero(size(arr)[1],size(arr)[0])
  for (let i = 0; i < arr[i].length; i++) {
    for (let j = 0; j < arr.length; j++) {
      res[i][j] = arr[j][i]
    }
  }
  return res
}
