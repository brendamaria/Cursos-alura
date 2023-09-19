import CardColaborador from '../CardColaborador';
import './Time.css';

const Time = (props) => {
    return (
        (props.colaboradores.length) > 0 ? <section className='time' style={{ backgroundColor: props.corSecundaria }}>
            <h3 style={{ borderColor: props.corPrincipal }}>{props.nome}</h3>
            <div className='coladoradores'>
                {props.colaboradores.map( colaborador => <CardColaborador key={colaborador.nome } colaborador={colaborador} corPrincipal={props.corPrincipal} corSecundaria={props.corSecundaria} /> )}
            </div>
        </section>
        : ''
    )
}

export default Time