import React from 'react';
import './App.css';
import { Route, Routes } from 'react-router-dom';
import { ROUTE_KEYS } from './utils/constants';
import Register from './pages/auth/register';
import Login from './pages/auth/login';
import MyPlantsLayout from './pages/my-plants';
import MyPlants from './pages/my-plants/features/my-plants';
import PlantDetails from './pages/my-plants/features/plants-details';
import MyPlantsFriendLayout from './pages/my-plant-friend';
import MyPlantFriend from './pages/my-plant-friend/features/my-plant-friend';
function App() {
  return (
    <div className=''>
      <Routes>
        <Route path={ROUTE_KEYS.LOGIN} element={<Login />} />
        <Route path={ROUTE_KEYS.REGISTER} element={<Register />} />
        <Route path={ROUTE_KEYS.PLANTS} element={<MyPlantsLayout />}>
          <Route index element={<MyPlants />} />
          <Route path={ROUTE_KEYS.PlANT_DETAILS} element={<PlantDetails />} />
        </Route>
        <Route path={ROUTE_KEYS.PLANT_FRIEND} element={<MyPlantsFriendLayout />}>
          <Route index element={<MyPlantFriend />} />
          <Route path={ROUTE_KEYS.PlANT_DETAILS} element={<PlantDetails />} />
        </Route>
      </Routes>
    </div>
  );
}

export default App;
