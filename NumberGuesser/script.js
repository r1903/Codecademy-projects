let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:

function generateTarget() {
    return Math.floor(Math.random()*10);
};

function compareGuesses(humanScore,computerScore,secretTargetNumber){
    if(humanScore < 0 || humanScore > 9)
        alert("Number is out of range!");
    let humanGuess = getAbsoluteDistance(humanScore,secretTargetNumber);
    let computerGuess = getAbsoluteDistance(computerScore,secretTargetNumber);
    if(humanGuess===computerGuess) {
        return true;
    } else if(computerGuess > humanGuess){
        return true;
    }else return false;
};

function getAbsoluteDistance(guessNum,targetNum){
    return Math.abs(guessNum-targetNum);
}

function updateScore(winner){
    winner === 'human'?humanScore+1:computerScore+1;
}

function advanceRound(){
    currentRoundNumber+=1;
}