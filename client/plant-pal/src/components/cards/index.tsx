import React, { ReactNode } from 'react';
import { PlantSuggestionType } from '../../pages/my-plants/features/modals/add-plants';
export const TitleCard = ({
  text,
  children,
  className
}: {
  text: string;
  children: ReactNode;
  className?: string;
}) => {
  return (
    <div
      className={`relative border-[1.3px] border-green-50  rounded-md p-6 py-14 sm:py-8 ${className}`}>
      <h6 className=' text-green-600 bg-white font-semibold absolute -top-[10.5px] sm:left-10 left-[50%] -translate-x-[50%] sm:-translate-x-0 bg-white-100 px-3 text-xs tracking-widest'>
        {text}
      </h6>
      {children}
    </div>
  );
};

export const DetailsCard = ({ title, details }: { title: string; details: string }) => {
  return (
    <div className='flex flex-col items-start gap-3'>
      <h6 className=' text-green-400 font-medium'> {title} </h6>
      <p className='text-sm'>{details}</p>
    </div>
  );
};

export const PlantCard = ({
  title,
  details,
  Img,
  onClick
}: {
  title: string;
  details: string;
  Img: string;
  onClick?: () => void;
}) => {
  return (
    <div
      className='cursor-pointer w-[250px] border border-green-30 rounded-md shadow-md  min-h-[280px]'
      onClick={onClick}>
      <div className='h-[180px] w-full'>
        <img
          src={Img}
          alt=''
          className='rounded-t-md h-[100%] w-[100%] object-cover object-center'
        />
      </div>
      <div className='p-4 flex flex-col items-start gap-3'>
        <h6 className=' text-green-400 font-medium'> {title} </h6>
        <p className='text-sm'>{details}</p>
      </div>
    </div>
  );
};

export const PlantSuggestionCard = ({
  list,
  onClick
}: {
  list: PlantSuggestionType;
  onClick?: () => void;
}) => {
  return (
    <div
      className='cursor-pointer w-[250px] border border-green-30 rounded-md shadow-md text-xs text-black font-semibold  min-h-[280px]'
      onClick={onClick}>
      <div className='h-[180px] w-full'>
        <img
          src={list?.Img}
          alt=''
          className='rounded-t-md h-[100%] w-[100%] object-cover object-center'
        />
      </div>
      <div className='p-4 gap-4 flex flex-col lists-start'>
        <h6 className='text-xs text-black'>
          {' '}
          COMMON NAME:{' '}
          {list?.Name?.map((itm, i) => (
            <span className={`capitalize`} key={i}>
              {itm}
              {list?.Name?.length - 1 !== i ? ', ' : ' '}
            </span>
          ))}
        </h6>
        <p>LATIN NAME: {list?.latinName}</p>
        <p className=''> CATEGORY: {list?.Category}</p>
      </div>
    </div>
  );
};
