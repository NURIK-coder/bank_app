import { useEffect } from "react";
import { useSelector } from "react-redux"
import { store } from "../store/store";
import { GetCardsList } from "../store/cards/cardActions";
import CardDetail from "./CardDetail";
import { useNavigate } from "react-router-dom";

function CardsList(){
    const cards = useSelector(card=>card.cardInfo.cards);
    const navigate = useNavigate();
    useEffect(()=>{
        store.dispatch(GetCardsList(navigate))
    }, [])
    

    return (
        <div className="flex flex-row flex-wrap gap-[30px] m-[50px]">
        
        {cards?.map((card, ind)=>(<CardDetail card={card} key={ind} />))}
        
        </div>
    )
}
export default CardsList;