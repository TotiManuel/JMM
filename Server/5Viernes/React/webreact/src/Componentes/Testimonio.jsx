import '../hojas-de-estilos/Testimonio.css';

export function Testimonio(props){
	return(
		<div className='contenedor-testimonio'>
			<img className='imagen-testimonio'
			src={require(`../Imagenes/web_${props.imagen}.png`)}
			alt='Foto de Usuario'/>
			<div className='contenedor-texto-testimonio'>
				<p className='nombre-pais-testimonio'>
				<strong>{props.nombre}</strong> ({props.pais})
				</p>
				<p className='cargo-testimonio'>
				Desarrollador {props.lenguajes}
				</p>
				<p className='texto-testimonio'>
				{props.testimonio}
				</p>
			</div>
		</div>
	);
}
