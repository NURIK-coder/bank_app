import { useEffect } from "react";
import { store } from "../store/store";
import { userRegister } from "../store/user/userAction";
import { Link } from "react-router-dom";

function Register(){
    

    const register = (e)=>{
        e.preventDefault();
        const RegisterForm = document.forms[0];
        const first_name = RegisterForm.first_name;
        const username = RegisterForm.username;
        const phone = RegisterForm.phone;
        const password = RegisterForm.password;
        const avatar = RegisterForm.avatar;


        const userdata = {
            first_name: first_name.value,
            username: username.value,
            phone: phone.value,
            password: password.value,
            avatar: avatar.files[0]
        }
        store.dispatch(userRegister(userdata))

    }
    return(
        <div>
           <form className="mt-[10vh] flex flex-wrap flex-col flex-wrap gap-[10px] w-[30em] m-auto rounded-[20px] border-2 border-solid border-[black]" action="" onSubmit={register}>
                <h2 className="text-xl">Sing up</h2>
                <label htmlFor="first_name">First name</label>
                <input className="w-[200px] border-2 border-solid border-[black] m-auto rounded-[20px]" type="text" name="first_name" id="" /><br /><br />

                <label htmlFor="username">Username</label>
                <input className="w-[200px] border-2 border-solid border-[black] m-auto rounded-[20px]" type="text" name="username" id="" /><br /><br />

                <label htmlFor="phone">Phone number</label>
                <input className="w-[200px] border-2 border-solid border-[black] m-auto rounded-[20px]" type="text" name="phone" id="" /><br /><br />

                <label htmlFor="password">Password</label>
                <input className="w-[200px] border-2 border-solid border-[black] m-auto rounded-[20px]" type="password" name="password" id="" /><br /><br />

                <label htmlFor="avatar">User avatar</label>
                <input className="w-[300px] border-2 border-solid border-[black] m-auto rounded-[20px]" type="file" name="avatar" id="" /><br /><br />


                <button className=" m-auto w-[200px] bg-[black] text-center text-[white] mt-5 p-5 rounded-[30px]" type="submit">Sumbit</button><br /><br />
                <span>If you have an account you can  <Link to='/login'><u>Sing in</u></Link></span>

            </form> 
        </div>
    )
}

export default Register;