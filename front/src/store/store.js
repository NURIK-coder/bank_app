import { combineReducers , createStore, applyMiddleware} from 'redux'
import { thunk } from 'redux-thunk'
import { userReduser } from './user/userReduser'
import { cardReduser } from './cards/cardReduser'


const rootReduser = combineReducers(
    {
        userInfo: userReduser,
        cardInfo: cardReduser
    }
)

export const store = createStore(rootReduser, applyMiddleware(thunk))