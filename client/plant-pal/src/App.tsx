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
import UnauthRoute from './router/UnauthRoute';
import AuthRoute from './router/AuthRoute';
function App() {
  return (
    <div className=''>
      <Routes>
        <Route
          path={ROUTE_KEYS.LOGIN}
          element={
            <UnauthRoute>
              <Login />
            </UnauthRoute>
          }
        />
        <Route
          path={ROUTE_KEYS.REGISTER}
          element={
            <UnauthRoute>
              <Register />
            </UnauthRoute>
          }
        />
        <Route
          path={ROUTE_KEYS.MY_PLANTS}
          element={
            <AuthRoute>
              <MyPlantsLayout />
            </AuthRoute>
          }>
          <Route
            index
            element={
              <AuthRoute>
                <MyPlants />
              </AuthRoute>
            }
          />
          <Route
            path={ROUTE_KEYS.PlANT_DETAILS}
            element={
              <AuthRoute>
                <PlantDetails />
              </AuthRoute>
            }
          />
        </Route>
        <Route
          path={ROUTE_KEYS.PLANT_FRIEND}
          element={
            <AuthRoute>
              <MyPlantsFriendLayout />
            </AuthRoute>
          }>
          <Route
            index
            element={
              <AuthRoute>
                <MyPlantFriend />
              </AuthRoute>
            }
          />
          <Route
            path={ROUTE_KEYS.PlANT_DETAILS}
            element={
              <AuthRoute>
                <PlantDetails />
              </AuthRoute>
            }
          />
        </Route>
      </Routes>
    </div>
  );
}

export default App;
