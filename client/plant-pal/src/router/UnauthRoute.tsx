import React from 'react';
import { Navigate } from 'react-router-dom';
import { ROUTE_KEYS, STORAGE_KEYS } from '../utils/constants';

const UnauthRoute = ({ children }: { children: JSX.Element }) => {
  const token = localStorage.getItem(STORAGE_KEYS.USER_ID);
  return !token ? children : <Navigate to={ROUTE_KEYS.MY_PLANTS} />;
};
export default UnauthRoute;
