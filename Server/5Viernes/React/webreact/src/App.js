import logo from './logo.svg';
import './App.css';
import {Testimonio} from './Componentes/Testimonio.jsx';

function App() {
  return (
    <div className="App">
      <div className='contenedor-principal'>
      <h1>Julian Manuel Mandaio</h1>
      <Testimonio 
      imagen='logo'
      nombre='Julian Manuel Mandaio'
      pais='Argentina'
      lenguajes='Web y de Python'
      testimonio='"Soy un Programador Autodidacta de 24 años de edad. Aprendi de manera autodidacta pero busco la oportunidad de desarrollarme como programador de una manera mas profesional."'/>
      <Testimonio 
      imagen='logo'
      nombre='Pasatiempos'
      pais='Relacionados'
      lenguajes='CiberSeguridad'
      testimonio='"Soy un Programador Autodidacta de 24 años de edad. Aprendi de manera autodidacta pero busco la oportunidad de desarrollarme como programador de una manera mas profesional."'/>
      </div>
    </div>
  );
}

export default App;
