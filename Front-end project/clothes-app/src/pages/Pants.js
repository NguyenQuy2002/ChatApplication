import React, { useState } from 'react';
import data from '../data/pants';

const Pants = () => {
	const [items, setItems] = useState(data);
	return (
		<>
			<h1 className='py-10 text-center font-bold text-4xl'>Pants</h1>
			<section className='p-5 grid grid-cols-1 gap-10 sm:grid-cols-2 lg:grid-cols-3 2xl:grid-cols-4'>
				{items.map((item) => {
					const { id, image, title, desc, category, type, price } =
						item;

					return (
						<div
							key={id}
							className='bg-gray-200'>
							<img
								src={image}
								alt={title}
							/>
							<div className='flex align-items-center justify-content-between'>
								<div className='px-5'>
									<h2 className='font-bold mt-5'>{title}</h2>
									<p>{desc}</p>
								</div>
							</div>

							<div className='my-2 px-5'>
								<small className='bg-green-500 rounded-full px-2 text-white tracking-widest mr-3'>
									{type}
								</small>
								<small className='bg-green-500 rounded-full px-2 text-white tracking-widest mr-3'>
									{category}
								</small>
							</div>
							<div className='flex flex-row'>
								<p className='text-2xl px-5 pb-10'>${price}</p>
								<button className='text-2xl px-5 border-2 border-green-400 bg-green-400'>
									Buy
								</button>
							</div>
						</div>
					);
				})}
			</section>
		</>
	);
};

export default Pants;
