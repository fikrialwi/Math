function isPrime(e) {
  if(e < 2){
    return false
  }
    for(let i = 2; i < e; i++){
    if(e%i === 0){
        return false
      }
    }
    return true
}



function genPrime(e) {
  if(e < 2){
    return "tidak ada. bilangan prima lebih dari sama dengan 2"
  }
  let result = []
  for(let i = 0; i <= e;i++){
    if(isPrime(i)){
      result.push(i)
    }
  }
  return result
}
