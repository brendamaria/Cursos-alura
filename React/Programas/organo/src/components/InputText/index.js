import './InputText.css'

const InputText = (props) => {

    const aoDigitado = (evento) => {
        props.aoAlterado(evento.target.value);
    }

    return (
        <div className="input-text" >
            <label>{ props.label }</label>
            <input value={props.value} onChange={aoDigitado} required={props.obrigatorio} placeholder={ props.placeholder } />
        </div>
    )
}

export default InputText