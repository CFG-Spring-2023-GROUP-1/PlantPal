import React, { FC } from 'react';
import { BsPeopleFill } from 'react-icons/bs';

type ProfileColor = 'pink' | 'blue';

type ProfileIconProps = {
  color?: ProfileColor;
  img?: string;
  big?: boolean;
  active?: boolean;
};
const ProfileIcon: FC<ProfileIconProps> = ({
  color = 'pink',
  img,
  big = false,
  active = false
}) => {
  return (
    <div
      className={` border-[2px] relative ${
        big ? 'w-10 h-10' : ' w-8 h-8'
      } rounded-[100%] flex items-center justify-center ${
        color === 'blue' ? 'border-blue-100' : color === 'pink' && '  border-pink-100'
      }`}>
      {img ? <img src={img} alt='' className='w-[95%] h-[95%]' /> : <BsPeopleFill size={25} />}

      {active && (
        <div className='absolute top-[.5px] -right-[.5px] w-2 h-2 rounded-full bg-green-4'></div>
      )}
    </div>
  );
};

export default ProfileIcon;
