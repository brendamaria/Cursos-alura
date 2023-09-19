import "./Card.css"
import InputText from "../InputText"
import Dropdown from "../Dropdown"
import Button from "../Button"
import { useState } from 'react'


const Card = (props) => {

    const [nome, setNome] = useState('');
    const [cargo, setCargo] = useState('');
    const [imagem, setImagem] = useState('');
    const [time, setTime] = useState('');

    const salvar = (evento) => {
        evento.preventDefault()
        props.aoCadastrarColaborador({
            nome,
            cargo,
            imagem,
            time
        });
        setNome('');
        setCargo('');
        setImagem('');
        setTime('');
    }

    return(
        <section className="card">
            <form onSubmit={salvar}>
                <h2>Preencha os dados para criar o card do colaborador.</h2>
                <InputText value={nome} aoAlterado={valor => setNome(valor)} obrigatorio={true} label="Nome" placeholder="Digite seu nome"/>
                <InputText value={cargo} aoAlterado={valor => setCargo(valor)} obrigatorio={true} label="Cargo" placeholder="Digite seu cargo"/>
                <InputText value={imagem} aoAlterado={valor => setImagem(valor)} obrigatorio={false} label="Imagem" placeholder="Informe o endereço da imagem"/>
                <Dropdown value={time} aoAlterado={valor => setTime(valor)} obrigatorio={true} label="Time" itens={props.times} />
                <Button>Criar card</Button>
            </form>
        </section>
    )
}

export default Card