import axios from "axios";


const URL = ' http://127.0.0.1:8000/user/'



export const userRegister = (userdata)=>{
    return async (dispatch)=>{


        const fd = new FormData();
        fd.append('username', userdata.username);
        fd.append('first_name', userdata.first_name);
        fd.append('password', userdata.password);
        fd.append('avatar', userdata.avatar);
        const response = await fetch(URL+'register/', {
            method: 'POST',
            body: fd    
            
        });
        const data = await response.json()
        dispatch({type: 'SET_USER', payload: data.user})
    }
}

export const userLogin = (userLoginData, navigate)=>{

    return async (dispatch)=>{
        const response = await fetch(URL+'login/', {
            method: 'POST',
            headers:{
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(userLoginData)
            
        })
        const data = await response.json();
        localStorage.setItem('token', data.access);
        navigate('/home')
        
        
        dispatch({type: 'SET_USER', payload: data.user})    
    }
}

export const GetCurrentUser = ()=>{
    return async (dispatch)=>{
        try {
            const response = await axios.get(URL+'current/', {
                headers:{
                    'Authorization': `Bearer ${localStorage.getItem('token')}`
                }
            })
            
            const data = response.data
            dispatch({type: 'SET_USER', payload: data})
            return "success"
        }
        catch (err){
            if (err.status == 401){  
                
            }
        }
    }
}