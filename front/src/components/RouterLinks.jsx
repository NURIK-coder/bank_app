import { BrowserRouter, Route, Routes } from "react-router-dom";
import Register from "./Register";
import Layout from "./Layout";
import Login from "./Login";
import Home from "../pages/Home";
import LoginPage from "../pages/LoginPage";
import RegisterPage from "../pages/RegisterPage";
import CardsListPage from "../pages/CardsListPage";
import Error from '../pages/Error'

function RouterLinks(){
    

    return(
        <BrowserRouter>
                <Routes>
                    <Route  path='/' element={<Layout/>}>
                        <Route
                        path='/login'
                        element={<LoginPage/>}
                        />
                        <Route
                        path='/register'
                        element={<RegisterPage/>}   
                        />
                        <Route
                        path="/home"
                        element={<Home/>}
                        />
                        <Route
                        path="/cards/list"
                        element={<CardsListPage/>}
                        />
                        <Route
                        path='*'
                        element={<Error/>}
                        />
                    </Route>
                </Routes>
            </BrowserRouter>
    )
}
export default RouterLinks;