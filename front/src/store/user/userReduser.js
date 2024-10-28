const InitialState = {
    user: {},
}

export const userReduser = (state=InitialState, action)=>{
    switch(action.type){
        case 'SET_USER':
            return{...state, user: action.payload}
        default:
            return state
    }
}