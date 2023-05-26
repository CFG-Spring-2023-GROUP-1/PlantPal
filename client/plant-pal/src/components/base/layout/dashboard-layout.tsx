import React, { ReactNode } from 'react';
import SideBar, { ActiveType } from '../../sidebar';
import NavBar from '../../navbar';

const DashboardLayout = ({ children, active }: { children: ReactNode; active: ActiveType }) => {
  return (
    <div className=' flex '>
      <SideBar active={active} />
      <div className=' w-full h-[100vh] overflow-y-scroll'>
        <NavBar />

        {children}
      </div>
    </div>
  );
};

export default DashboardLayout;
