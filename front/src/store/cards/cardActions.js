import axios from "axios"
import { useNavigate } from "react-router-dom"

const URL = 'http://127.0.0.1:8000/cards/'


export const GetCardsList = (navigate)=>{
    return async (dispatch)=>{
        try{
            const response = await axios.get(URL+`list/`, {
                headers:{
                    'Authorization': `Bearer ${localStorage.getItem('token')}`
                }
            })
            const data = response.data
            
            dispatch({type: 'SET_CARDS', payload: data})
            return "success"
        }catch(err){
            if (err.status == 401){
                navigate('/login')
            }else{
                navigate('/error')
            }
        }
    }
}