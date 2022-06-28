import React from 'react'
import '../Styles/kills.css';

function kills(props){
	return(
		<div className='contenedor-imagen'>
			<img className='imagen-cv'
			src={require(`../Images/${props.imagen}.png`)}
			alt='Foto de Usuario' />
		</div>
	);
}
export default kills;
