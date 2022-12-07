import React from 'react';
import { NavLink } from 'react-router-dom';
// eslint-disable-next-line
const Header = () => {
	return (
		<>
			<nav className='bg-green-400 py-3'>
				<ul className='flex justify-center'>
					<li className='mx-5 uppercase font-bold'>
						<NavLink
							className='transition-colors hover:text-green-900 text-white'
							to='/'>
							Home
						</NavLink>
					</li>
					<li className='mx-5 uppercase font-bold'>
						<NavLink
							className='transition-colors hover:text-green-900 text-white'
							to='/products'>
							Products
						</NavLink>
					</li>
					<li className='mx-5 uppercase font-bold'>
						<NavLink
							className='transition-colors hover:text-green-900 text-white'
							to='/dresses'>
							Dresses
						</NavLink>
					</li>
					<li className='mx-5 uppercase font-bold'>
						<NavLink
							className='transition-colors hover:text-green-900 text-white'
							to='/pants'>
							Pants
						</NavLink>
					</li>
					<li className='mx-5 uppercase font-bold'>
						<NavLink
							className='transition-colors hover:text-green-900 text-white'
							to='/Shirts'>
							Shirts
						</NavLink>
					</li>
				</ul>
			</nav>
		</>
	);
};

export default Header;
