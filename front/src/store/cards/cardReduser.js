const InitialState = {
    cards: [],
    card: {}
}

export const cardReduser = (state=InitialState, action) =>{
    switch (action.type){
        case 'SET_CARDS':
            return {...state, cards: action.payload}
        case "SET_CARD":
            return {...state, card: action.payload}
        default:
            return state
    }
}