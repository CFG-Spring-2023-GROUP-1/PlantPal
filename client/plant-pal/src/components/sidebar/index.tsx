import React from 'react';
import { Link } from 'react-router-dom';
import Logo from '../../assets/Logo';
import { SIDE_BAR } from '../../utils/constants';
import { BiLogOut } from 'react-icons/bi';

export type ActiveType = 'my plants' | 'profile' | 'my plant friend';

const SideBar = ({ active }: { active: ActiveType }) => {
  return (
    <div className=' hidden md:block pt-6 w-[180px] md:w-[270px] border-r border-blue-200 h-[100vh] '>
      <div className='pl-3'>
        <Logo />
      </div>

      <div className=' flex flex-col  justify-between h-[80vh] mt-6'>
        <div className='space-y-6 mt-6'>
          {SIDE_BAR.map((item, i) => {
            return (
              <Link
                key={i}
                to={item?.route}
                className={`flex items-center  cursor-pointer text-green-200 text-[15px] font-medium pl-3 transition-all  ${
                  active === item?.title
                    ? 'pl-5 bg-brown-100 border-l-4 py-2 border-l-green-800 text-opacity-90  gap-3 '
                    : ' text-opacity-50 gap-2'
                } `}>
                {item.icon}
                <p
                  className={`text-green-500 ${
                    active === item?.title ? 'font-bold' : 'font-medium'
                  } text-opacity-80 capitalize`}>
                  {item.title}{' '}
                </p>
              </Link>
            );
          })}
        </div>

        <div className='mt-auto flex text-red-500 items-center pl-3 font-bold gap-3 cursor-pointer'>
          <BiLogOut />
          Logout
        </div>
      </div>
    </div>
  );
};

export default SideBar;
