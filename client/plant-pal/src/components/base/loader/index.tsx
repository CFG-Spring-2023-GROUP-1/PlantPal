import React from 'react';
import { BiLoaderAlt } from 'react-icons/bi';

const Loader = ({ size = 16, className }: { size?: number; className?: string }) => {
  return (
    <BiLoaderAlt
      className={`animate-spin flex justify-center mx-auto text-white my-6 ${className}`}
      size={size}
    />
  );
};

export default Loader;
