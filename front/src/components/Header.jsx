import { useEffect } from "react";
import { store } from "../store/store";
import { GetCurrentUser } from "../store/user/userAction";
import { useSelector } from "react-redux";
import { Link } from "react-router-dom";

function Header(){
    const user = useSelector(u=>u.userInfo.user);
    useEffect(()=>{
        store.dispatch(GetCurrentUser())
    }, [])
    return(
        <div className="bg-[cyan] rounded-[20px] p-[50px]">
            <h1 className="text-[30px]">Hello {user?.first_name}</h1>
            {/* <Link className="bg-[black] text-left text-[white] mt-5  p-5 rounded-[30px] " to='/cards/list/'>Cards list</Link> */}
        </div>
    )
}
export default Header;
