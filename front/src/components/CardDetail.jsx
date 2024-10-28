import { useNavigate } from "react-router-dom";

function CardDetail(card){
    const navigate = useNavigate();
    return(
        <div onClick={navigate('/detail')} className="text-left w-[300px] h-[150px] p-[30px] shadow-[rgba(14,30,37,0.12)_0px_2px_4px_0px,rgba(14,30,37,0.32)_0px_2px_16px_0px] p-[30px] rounded-[20px] border-solid border-[black]">
            <h1>{card.card.card_num}</h1>
            <p>{card.card.deadline}</p>
        </div>
    )
}
export default CardDetail;