import Card from './components/Card';
import Header from './components/Header';
import { useState } from 'react'
import Time from './components/Time';
import Footer from './components/Footer';


function App() {

  const times = [
    {
      nome: 'Programação',
      corPrincipal: '#57C278',
      corSecundaria: '#D9F7E9',
    },
    {
      nome: 'Front-End',
      corPrincipal: '#82CFFA',
      corSecundaria: '#E8F8FF',
    },
    {
      nome: 'Data Science',
      corPrincipal: '#A6D157',
      corSecundaria: '#F0F8E2',
    },
    {
      nome: 'Devops',
      corPrincipal: '#E06B69',
      corSecundaria: '#FDE7E8',
    },
    {
      nome: 'UX e Design',
      corPrincipal: '#DB6EBF',
      corSecundaria: '#FAE9F5',
    },
    {
      nome: 'Mobile',
      corPrincipal: '#FFBA05',
      corSecundaria: '#FFF5D9',
    },
    {
      nome: 'Inovação e Gestão',
      corPrincipal: '#FF8A29',
      corSecundaria: '#FFEEDF',
    }
  ]

  const [colaboradores, setColaboradores] = useState([]);

  const novoColaboradorAdicionado = (colaborador) => {
    setColaboradores([...colaboradores, colaborador]);
  }

  return (
    <div>
      <Header />
      <Card aoCadastrarColaborador={colaborador => novoColaboradorAdicionado(colaborador)} times={times.map(time => time.nome)} />
      {times.map(time => 
        <Time key={time.nome} 
              nome={time.nome} 
              corPrincipal={time.corPrincipal} 
              corSecundaria={time.corSecundaria} 
              colaboradores={colaboradores.filter( c => c.time === time.nome )}
        />)}
      <Footer />
    </div>
  );
}

export default App;
