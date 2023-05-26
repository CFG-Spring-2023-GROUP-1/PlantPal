import React from 'react';
import DashboardLayout from '../../components/base/layout/dashboard-layout';
import { Outlet } from 'react-router-dom';

const MyPlantsFriendLayout = () => {
  return (
    <DashboardLayout active='my plant friend'>
      <div className='p-10'>
        <Outlet />
      </div>
    </DashboardLayout>
  );
};

export default MyPlantsFriendLayout;
