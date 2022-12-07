import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Dresses from './pages/Dresses';
import Products from './pages/Products'
import Pants from './pages/Pants'
import Shirts from './pages/Shirts';
import Home from './pages/Home';

const App = () => {
	return (
		<div>
			<Router>
				<div>
					<Header />
					<Routes>
						<Route
							path='/'
							element={<Home />}></Route>
						<Route
							path='/products'
							element={<Products />}></Route>
						<Route
							path='/dresses'
							element={<Dresses />}></Route>
						<Route
							path='/pants'
							element={<Pants />}></Route>
						<Route
							path='/shirts'
							element={<Shirts />}></Route>
					</Routes>
				</div>
			</Router>
		</div>
	);
};

export default App;
