import React from 'react';
import DashboardLayout from '../../components/base/layout/dashboard-layout';
import { Outlet } from 'react-router-dom';

const MyPlantsLayout = () => {
  return (
    <DashboardLayout active='my plants'>
      <div className='p-10'>
        <Outlet />
      </div>
    </DashboardLayout>
  );
};

export default MyPlantsLayout;
