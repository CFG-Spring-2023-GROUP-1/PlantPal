import React from 'react';

const Logo = ({ small, className }: { small?: boolean; className?: string }) => {
  return (
    <h1
      className={`text-green-100 font-bold font-kaushan tracking-[2px] ${
        small ? 'text-2xl' : 'text-3xl'
      } ${className}`}>
      PlantPal
    </h1>
  );
};

export default Logo;
