import './Descricao.css'

function Descricao(props) {
    return (
        <div className="descricao" >
            <label>{props.label}</label>
            <textarea required={props.obrigatorio} placeholder={props.placeholder} rows="10" cols="50" />
        </div>
    )
}

export default Descricao