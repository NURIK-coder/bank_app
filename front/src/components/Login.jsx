import { useEffect } from "react";
import { store } from "../store/store";
import { GetCurrentUser, userLogin } from "../store/user/userAction";
import { useSelector } from "react-redux";
import { Link, useNavigate } from "react-router-dom";

function Login(){
    const curr_user = useSelector(state => state.userInfo.user)
    const navigate = useNavigate();
    useEffect(()=>{
        if (curr_user?.id) {
            navigate('/home')
        }

        
    }, [curr_user])
    

    const login = (e)=>{
        e.preventDefault();
       
        const LoginForm = document.forms[0];
        const username = LoginForm.username;
        
        const password = LoginForm.password;

        const userLoginData = {
            username: username.value,
            password: password.value
        }
        store.dispatch(userLogin(userLoginData, navigate))
    }
    return(
        <div>
           <form className="mt-[10vh] flex flex-wrap flex-col flex-wrap gap-[30px] w-[30em] m-auto rounded-[20px] border-2 border-solid border-[black]" action="" onSubmit={login}>
            <h2 className="text-[30px]">Sing in</h2>
                <label className="text-xl" htmlFor="username">Username</label>
                <input className="w-[200px] border-2 border-solid border-[black] m-auto rounded-[20px]" type="text" name="username"placeholder="user1234" />
                <label className="text-xl" htmlFor="password">Password</label>
                <input className=" w-[200px] border-2 border-solid border-[black] m-auto rounded-[20px]" placeholder="*******" type="password" name="password" id="" />

                <button className=" m-auto w-[200px] bg-[black] text-center text-[white] mt-5 p-5 rounded-[30px]" type="submit">Sumbit</button>
                <span>If you don't have account you can  <Link to='/register'><u>Sing up</u></Link></span>
            </form> 
        </div>
    )
}

export default Login;