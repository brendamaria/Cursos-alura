import './CardColaborador.css';

const CardColaborador = (props) => {
    return (
        <div className='cardColaborador'>
            <div className='cabecalho' style={{ backgroundColor: props.corPrincipal}}>
                <img alt={props.colaborador.nome} src={props.colaborador.imagem}></img>
            </div>
            <div className='rodape' >
                <h4>{props.colaborador.nome}</h4>
                <h5>{props.colaborador.cargo}</h5>
            </div>
        </div>
    )
}

export default CardColaborador