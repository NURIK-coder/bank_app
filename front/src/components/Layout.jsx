import { useEffect } from "react";
import { Outlet, useNavigate } from "react-router-dom"
import { store } from "../store/store";
import { GetCurrentUser } from "../store/user/userAction";
import Header from "./Header";
import Footer from "./Footer";
function Layout(){
    useEffect(() => {
        store.dispatch(GetCurrentUser())
    }, [])
    return(
        <div>
            <header>
                <Header />
            </header>
            
            <Outlet/>

            <footer>
                <Footer/>
            </footer>
        </div>
    )
}

export default Layout;